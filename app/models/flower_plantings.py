from sqlalchemy import Column, Integer, String, Text, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class FlowerPlanting(Base):
    __tablename__ = "flower_planting"

    id = Column(Integer, primary_key=True)
    flower_id = Column(Integer, ForeignKey("flower_base.id"))
    bed_id = Column(Integer, ForeignKey("beds.id"))
    action_id = Column(Integer, ForeignKey("bed_actions.id"))
    quantity_planted = Column(Integer)

    flower = relationship("FlowerBase", back_populates="plantings")
    bed = relationship("Bed", back_populates="plantings")
    action = relationship("BedAction", back_populates="plantings")