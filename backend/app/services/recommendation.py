# app/services/recommendation.py
from sqlalchemy.orm import Session
from app import models
from app.services.fit_scoring import recommend_size

CATEGORY_TO_TYPE = {
    "hoodie": "top", "tee": "top", "jacket": "top",
    "jeans": "bottom",
    "sneakers": None,  # no meaningful chest/waist sizing
}

def score_style_match(clothing_tags: str, style_profile: dict) -> float:
    tags = [t.strip() for t in clothing_tags.split(",")]
    return sum(style_profile.get(tag, 0) for tag in tags)

def pick_best_item(db: Session, category: str, style_profile: dict):
    items = db.query(models.Clothing).filter(models.Clothing.category == category).all()
    if not items:
        return None
    scored = [(item, score_style_match(item.style_tags, style_profile)) for item in items]
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[0][0]  # highest-scoring item

def build_item_response(db: Session, clothing, user, fit_preference="regular"):
    sizes = db.query(models.ClothingSize).filter(models.ClothingSize.clothing_id == clothing.id).all()
    size_chart = [
        {"size": s.size, "chest": s.chest, "waist": s.waist}
        for s in sizes
    ]

    category_type = CATEGORY_TO_TYPE.get(clothing.category)
    if category_type == "top":
        fit_result = recommend_size(user.chest, size_chart, fit_preference, "top")
    elif category_type == "bottom":
        fit_result = recommend_size(user.waist, size_chart, fit_preference, "bottom")
    else:
        fit_result = {"recommended_size": sizes[0].size if sizes else None, "confidence": 1.0, "fit_score": 100}

    return {
        "id": clothing.id,
        "name": clothing.name,
        "brand": clothing.brand,
        "price": clothing.price,
        "image": clothing.image_url,
        "recommended_size": fit_result["recommended_size"],
        "fit_score": fit_result["fit_score"],
    }

def generate_outfit(db: Session, user_id: int, fit_preference: str = "regular"):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    style_profile_row = db.query(models.StyleProfile).filter(models.StyleProfile.user_id == user_id).first()

    style_profile = {}
    if style_profile_row:
        style_profile = {
            "streetwear": style_profile_row.streetwear,
            "casual": style_profile_row.casual,
            "minimal": style_profile_row.minimal,
            "preppy": style_profile_row.preppy,
            "formal": style_profile_row.formal,
            "techwear": style_profile_row.techwear,
        }

    top = pick_best_item(db, "hoodie", style_profile) or pick_best_item(db, "tee", style_profile)
    bottom = pick_best_item(db, "jeans", style_profile)
    shoes = pick_best_item(db, "sneakers", style_profile)

    if not (top and bottom and shoes and user):
        return None

    return {
        "outfit_id": 1,  # placeholder — could increment/store real outfit records later
        "top": build_item_response(db, top, user, fit_preference),
        "bottom": build_item_response(db, bottom, user, fit_preference),
        "shoes": build_item_response(db, shoes, user, fit_preference),
    }