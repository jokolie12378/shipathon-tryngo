from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.routers import clothing

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FitSwipe API")

@app.get("/")
def root():
    return {"status": "FitSwipe API running"}

app.include_router(clothing.router)