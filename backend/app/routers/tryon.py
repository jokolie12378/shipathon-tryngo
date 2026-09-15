# app/routers/tryon.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app.services.fit_scoring import recommend_size

router = APIRouter(prefix="/tryon", tags=["tryon"])

CATEGORY_TO_TYPE = {
    "hoodie": "top", "tee": "top", "jacket": "top",
    "jeans": "bottom",
    "sneakers": None,
}

@router.get("/{clothing_id}")
def get_tryon_data(clothing_id: int, user_id: int, fit_preference: str = "regular", db: Session = Depends(get_db)):
    clothing = db.query(models.Clothing).filter(models.Clothing.id == clothing_id).first()
    if not clothing:
        raise HTTPException(status_code=404, detail="Clothing not found")

    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    sizes = db.query(models.ClothingSize).filter(models.ClothingSize.clothing_id == clothing.id).all()
    size_chart = [{"size": s.size, "chest": s.chest, "waist": s.waist} for s in sizes]

    category_type = CATEGORY_TO_TYPE.get(clothing.category)
    if category_type == "top":
        fit_result = recommend_size(user.chest, size_chart, fit_preference, "top")
    elif category_type == "bottom":
        fit_result = recommend_size(user.waist, size_chart, fit_preference, "bottom")
    else:
        fit_result = {"recommended_size": sizes[0].size if sizes else None, "confidence": 1.0}

    return {
        "clothing_id": clothing.id,
        "category": clothing.category,       # P3 uses this to pick which 3D asset to load
        "fit_type": clothing.fit_type,
        "recommended_size": fit_result["recommended_size"],
        "avatar_measurements": {
            "height": user.height,
            "chest": user.chest,
            "waist": user.waist,
            "hips": user.hips,
            "inseam": user.inseam,
            "shoulders": user.shoulders,
        },
    }