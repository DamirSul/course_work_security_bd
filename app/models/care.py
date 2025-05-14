from sqlalchemy import Column, Integer, String, Text, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Care(Base):
    __tablename__ = "care"

    id = Column(Integer, primary_key=True)
    care_name = Column(String)

    bed_actions = relationship("BedAction", back_populates="care")