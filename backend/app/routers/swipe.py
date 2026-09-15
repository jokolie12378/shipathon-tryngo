# app/routers/swipe.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/swipe", tags=["swipe"])

@router.post("/")
def create_swipe(data: schemas.SwipeIn, db: Session = Depends(get_db)):
    swipe = models.Swipe(
        user_id=data.user_id,
        clothing_id=data.clothing_id,
        direction=data.direction,
    )
    db.add(swipe)
    db.commit()
    db.refresh(swipe)
    return {"status": "logged", "swipe_id": swipe.id}
