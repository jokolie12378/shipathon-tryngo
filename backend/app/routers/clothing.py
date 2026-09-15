# app/routers/clothing.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from app.services.recommendation import build_item_response

router = APIRouter(prefix="/clothing", tags=["clothing"])

@router.post("/", response_model=schemas.ClothingDetailOut)
def create_clothing(item: schemas.ClothingIn, db: Session = Depends(get_db)):
    clothing = models.Clothing(
        brand=item.brand,
        name=item.name,
        category=item.category,
        fit_type=item.fit_type,
        style_tags=item.style_tags,
        price=item.price,
        image_url=item.image_url,
        store_id=item.store_id,
    )
    db.add(clothing)
    db.commit()
    db.refresh(clothing)

    for s in item.sizes:
        size = models.ClothingSize(
            clothing_id=clothing.id,
            size=s.size,
            chest=s.chest,
            waist=s.waist,
            length=s.length,
            shoulder=s.shoulder,
            sleeve=s.sleeve,
        )
        db.add(size)
    db.commit()

    return clothing

@router.get("/", response_model=list[schemas.ClothingDetailOut])
def list_clothing(db: Session = Depends(get_db)):
    return db.query(models.Clothing).all()

@router.get("/next")
def get_next_item(
    user_id: int,
    fit_preference: str = "regular",
    exclude: str = "",
    db: Session = Depends(get_db),
):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    style_row = db.query(models.StyleProfile).filter(models.StyleProfile.user_id == user_id).first()
    style_profile = {}
    if style_row:
        style_profile = {
            "streetwear": style_row.streetwear, "casual": style_row.casual,
            "minimal": style_row.minimal, "preppy": style_row.preppy,
            "formal": style_row.formal, "techwear": style_row.techwear,
        }

    excluded_ids = [int(i) for i in exclude.split(",") if i.strip().isdigit()]

    already_swiped_ids = [
        row[0] for row in db.query(models.Swipe.clothing_id).filter(models.Swipe.user_id == user_id).all()
    ]
    all_excluded = set(excluded_ids + already_swiped_ids)

    query = db.query(models.Clothing)
    if all_excluded:
        query = query.filter(~models.Clothing.id.in_(all_excluded))
    candidates = query.all()

    if not candidates:
        raise HTTPException(status_code=404, detail="No more items to show")

    scored = [
        (item, sum(style_profile.get(t.strip(), 0) for t in item.style_tags.split(",")))
        for item in candidates
    ]
    scored.sort(key=lambda x: x[1], reverse=True)
    best_item = scored[0][0]

    return build_item_response(db, best_item, user, fit_preference)

@router.get("/{clothing_id}", response_model=schemas.ClothingDetailOut)
def get_clothing(clothing_id: int, db: Session = Depends(get_db)):
    clothing = db.query(models.Clothing).filter(models.Clothing.id == clothing_id).first()
    if not clothing:
        raise HTTPException(status_code=404, detail="Clothing not found")
    return clothing