from sqlalchemy import Column, Integer, String, Text, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True)
    scale = Column(String)
    title = Column(String)
    report_link = Column(String)

    notifications = relationship("SystemNotification", back_populates="report")