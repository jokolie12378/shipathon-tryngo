from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.routers import clothing, measurements, style, outfit

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tryngo API")

@app.get("/")
def root():
    return {"status": "Tryngo API running"}

app.include_router(clothing.router)
app.include_router(measurements.router)
app.include_router(style.router)
app.include_router(outfit.router)