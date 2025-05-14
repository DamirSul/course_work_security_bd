from sqlalchemy import Column, Integer, String, Text, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Bed(Base):
    __tablename__ = "beds"

    id = Column(Integer, primary_key=True)
    bed_name = Column(String)
    total_capacity = Column(Integer)
    current_occupancy = Column(Integer)

    agronomists = relationship("BedAgronomist", back_populates="bed")
    plantings = relationship("FlowerPlanting", back_populates="bed")
