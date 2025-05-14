from sqlalchemy import Column, Integer, String, Text, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class BedAction(Base):
    __tablename__ = "bed_actions"

    id = Column(Integer, primary_key=True)
    care_id = Column(Integer, ForeignKey("care.id"))
    action_date = Column(Date)
    labor_costs = Column(Float)

    care = relationship("Care", back_populates="bed_actions")
    plantings = relationship("FlowerPlanting", back_populates="action")