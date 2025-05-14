from sqlalchemy import Column, Integer, String, Text, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Agronomist(Base):
    __tablename__ = "agronomist"

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))

    employee = relationship("Employee", back_populates="agronomist")
    beds = relationship("BedAgronomist", back_populates="agronomist")