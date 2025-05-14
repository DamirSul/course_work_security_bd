from sqlalchemy import Column, Integer, String, Text, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class PurchasePlan(Base):
    __tablename__ = "purchase_plan"

    id = Column(Integer, primary_key=True)
    resource_id = Column(Integer, ForeignKey("resources.id"))
    quantity = Column(Integer)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    create_date = Column(Date)

    resource = relationship("Resource", back_populates="purchase_plans")
    employee = relationship("Employee", back_populates="purchase_plans")
    purchases = relationship("Purchase", back_populates="purchase_plan")