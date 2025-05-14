from sqlalchemy import Column, Integer, String, Text, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base



class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True)
    purchase_plan_id = Column(Integer, ForeignKey("purchase_plan.id"))
    create_date = Column(Date)

    purchase_plan = relationship("PurchasePlan", back_populates="purchases")