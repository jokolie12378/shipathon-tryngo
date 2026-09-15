# app/routers/measurements.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/measurements", tags=["measurements"])

@router.post("/")
def create_measurements(data: schemas.MeasurementsIn, db: Session = Depends(get_db)):
    user = models.User(
        height=data.height,
        chest=data.chest,
        waist=data.waist,
        hips=data.hips,
        inseam=data.inseam,
        shoulders=data.shoulders,
        photo_url=data.photo_url,
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "user_id": user.id,
        "height": user.height,
        "chest": user.chest,
        "waist": user.waist,
        "hips": user.hips,
        "inseam": user.inseam,
        "shoulders": user.shoulders,
    }