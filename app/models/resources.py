from sqlalchemy import Column, Integer, String, Text, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True)
    resource_name = Column(String)
    quantity_available = Column(Integer)

    purchase_plans = relationship("PurchasePlan", back_populates="resource")