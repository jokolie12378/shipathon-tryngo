# app/routers/buy.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models

router = APIRouter(prefix="/buy", tags=["buy"])

@router.get("/identify/{clothing_id}")
def identify_for_purchase(clothing_id: int, db: Session = Depends(get_db)):
    clothing = db.query(models.Clothing).filter(models.Clothing.id == clothing_id).first()
    if not clothing:
        raise HTTPException(status_code=404, detail="Clothing not found")

    store = None
    if clothing.store_id:
        store = db.query(models.Store).filter(models.Store.id == clothing.store_id).first()

    return {
        "clothing_id": clothing.id,
        "name": clothing.name,
        "brand": clothing.brand,
        "price": clothing.price,
        "image": clothing.image_url,
        "store": {
            "name": store.name if store else None,
            "address": store.address if store else None,
            "lat": store.lat if store else None,
            "lng": store.lng if store else None,
        } if store else None,
    }