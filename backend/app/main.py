from fastapi import FastAPI
from app.database import Base, engine
from app import models

# Create tables on startup (fine for SQLite/hackathon — no migrations needed)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FitSwipe API")

@app.get("/")
def root():
    return {"status": "FitSwipe API running"}