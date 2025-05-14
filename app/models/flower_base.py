from sqlalchemy import Column, Integer, String, Text, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class FlowerBase(Base):
    __tablename__ = "flower_base"

    id = Column(Integer, primary_key=True)
    flower_name = Column(String)
    variety = Column(String)
    color = Column(String)
    description = Column(Text)

    plantings = relationship("FlowerPlanting", back_populates="flower")