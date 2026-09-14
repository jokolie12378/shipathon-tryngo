from pydantic import BaseModel
from typing import Optional, List

class MeasurementsIn(BaseModel):
    height: float
    chest: float
    waist: float
    hips: float
    inseam: float
    shoulders: float
    photo_url: Optional[str] = None  # set if P3's photo pipeline produced this

class StyleAnswer(BaseModel):
    styles: dict[str, float]  # e.g. {"streetwear": 1, "casual": 0.5}

class StyleProfileIn(BaseModel):
    user_id: int
    answers: List[StyleAnswer]

class FitPreferenceIn(BaseModel):
    user_id: int
    category: str
    preferred_fit: str  # "oversized" | "regular" | "slim"

class SwipeIn(BaseModel):
    user_id: int
    outfit_id: int
    direction: str  # "left" | "right"

class FitFeedbackIn(BaseModel):
    user_id: int
    clothing_id: int
    size: str
    feedback: str  # "too_tight" | "good" | "too_loose"

# ---------- OUTPUT SCHEMAS ----------

class ClothingItemOut(BaseModel):
    id: int
    name: str
    brand: str
    price: float
    image: str
    recommended_size: str
    fit_score: int

    class Config:
        from_attributes = True

class OutfitOut(BaseModel):
    outfit_id: int
    top: ClothingItemOut
    bottom: ClothingItemOut
    shoes: ClothingItemOut

class ClothingDetailOut(BaseModel):
    id: int
    name: str
    brand: str
    category: str
    price: float
    image_url: str
    fit_type: str

    class Config:
        from_attributes = True

class StoreOut(BaseModel):
    id: int
    name: str
    address: str
    lat: float
    lng: float

    class Config:
        from_attributes = True