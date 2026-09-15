# app/routers/style.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/style", tags=["style"])

# Hardcoded quiz questions — fine for tonight, this is UI content, not user data
QUESTIONS = [
    {
        "question": "Which outfit would you wear?",
        "options": [
            {"image": "streetwear1.jpg", "styles": {"streetwear": 1, "casual": 0.5}},
            {"image": "preppy1.jpg", "styles": {"preppy": 1, "formal": 0.5}},
        ],
    },
    {
        "question": "Pick a vibe.",
        "options": [
            {"image": "minimal1.jpg", "styles": {"minimal": 1}},
            {"image": "techwear1.jpg", "styles": {"techwear": 1, "streetwear": 0.5}},
        ],
    },
    {
        "question": "Which fits your everyday style?",
        "options": [
            {"image": "casual1.jpg", "styles": {"casual": 1}},
            {"image": "formal1.jpg", "styles": {"formal": 1, "preppy": 0.5}},
        ],
    },
]

@router.get("/questions")
def get_questions():
    return QUESTIONS

@router.post("/profile")
def create_style_profile(data: schemas.StyleProfileIn, db: Session = Depends(get_db)):
    # Sum up style scores across all answers the user picked
    totals = {"streetwear": 0, "casual": 0, "minimal": 0, "preppy": 0, "formal": 0, "techwear": 0}
    for answer in data.answers:
        for style, value in answer.styles.items():
            if style in totals:
                totals[style] += value

    profile = models.StyleProfile(
        user_id=data.user_id,
        streetwear=totals["streetwear"],
        casual=totals["casual"],
        minimal=totals["minimal"],
        preppy=totals["preppy"],
        formal=totals["formal"],
        techwear=totals["techwear"],
    )
    db.add(profile)
    db.commit()
    db.refresh(profile)

    return {
        "user_id": data.user_id,
        "style_profile": totals,
    }