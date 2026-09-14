from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    height = Column(Float)        # inches
    chest = Column(Float)
    waist = Column(Float)
    hips = Column(Float)
    inseam = Column(Float)
    shoulders = Column(Float)
    photo_url = Column(String, nullable=True)  # set if P3's photo pipeline produced measurements/avatar ref

class StyleProfile(Base):
    __tablename__ = "style_profiles"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    streetwear = Column(Float, default=0)
    casual = Column(Float, default=0)
    minimal = Column(Float, default=0)
    preppy = Column(Float, default=0)
    formal = Column(Float, default=0)
    techwear = Column(Float, default=0)

class Clothing(Base):
    __tablename__ = "clothing"
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String)
    name = Column(String)
    category = Column(String)      # "hoodie", "tee", "jeans", "sneakers"
    fit_type = Column(String)      # "oversized", "regular", "slim"
    style_tags = Column(String)    # comma-separated: "streetwear,casual"
    price = Column(Float)
    image_url = Column(String)
    store_id = Column(Integer, ForeignKey("stores.id"))

    sizes = relationship("ClothingSize", back_populates="clothing")

class ClothingSize(Base):
    __tablename__ = "clothing_sizes"
    id = Column(Integer, primary_key=True, index=True)
    clothing_id = Column(Integer, ForeignKey("clothing.id"))
    size = Column(String)          # "S","M","L"
    chest = Column(Float, nullable=True)
    waist = Column(Float, nullable=True)
    length = Column(Float, nullable=True)
    shoulder = Column(Float, nullable=True)
    sleeve = Column(Float, nullable=True)

    clothing = relationship("Clothing", back_populates="sizes")

class FitPreference(Base):
    __tablename__ = "fit_preferences"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    category = Column(String)
    preferred_fit = Column(String)  # "oversized","regular","slim"

class FitFeedback(Base):
    __tablename__ = "fit_feedback"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    clothing_id = Column(Integer, ForeignKey("clothing.id"))
    size = Column(String)
    feedback = Column(String)  # "too_tight","good","too_loose"

class Swipe(Base):
    __tablename__ = "swipes"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    outfit_id = Column(Integer)
    direction = Column(String)  # "left","right"

class Store(Base):
    __tablename__ = "stores"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    lat = Column(Float)
    lng = Column(Float)