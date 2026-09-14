# app/routers/clothing.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

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

@router.get("/{clothing_id}", response_model=schemas.ClothingDetailOut)
def get_clothing(clothing_id: int, db: Session = Depends(get_db)):
    clothing = db.query(models.Clothing).filter(models.Clothing.id == clothing_id).first()
    if not clothing:
        raise HTTPException(status_code=404, detail="Clothing not found")
    return clothing