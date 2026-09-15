# app/routers/outfit.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.recommendation import generate_outfit

router = APIRouter(prefix="/outfit", tags=["outfit"])

@router.get("/generate")
def get_outfit(
    user_id: int = Query(...),
    fit_preference: str = Query("regular"),
    db: Session = Depends(get_db),
):
    outfit = generate_outfit(db, user_id, fit_preference)
    if not outfit:
        raise HTTPException(
            status_code=404,
            detail="Could not generate outfit — check that user exists and clothing catalog has items in every category",
        )
    return outfit