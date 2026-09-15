# app/routers/stores.py
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/stores", tags=["stores"])

class StoreIn(BaseModel):
    name: str
    address: str
    lat: float
    lng: float

@router.post("/", response_model=schemas.StoreOut)
def create_store(store: StoreIn, db: Session = Depends(get_db)):
    new_store = models.Store(
        name=store.name,
        address=store.address,
        lat=store.lat,
        lng=store.lng,
    )
    db.add(new_store)
    db.commit()
    db.refresh(new_store)
    return new_store

@router.get("/{store_id}", response_model=schemas.StoreOut)
def get_store(store_id: int, db: Session = Depends(get_db)):
    store = db.query(models.Store).filter(models.Store.id == store_id).first()
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    return store