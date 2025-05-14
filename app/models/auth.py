from sqlalchemy import Column, Integer, String, Text, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class EmployeeAuth(Base):
    __tablename__ = "employee_auth"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), unique=True, nullable=False)
    access_code = Column(String, unique=True, nullable=False)
    role = Column(String, nullable=False) 

    employee = relationship("Employee", back_populates="auth")