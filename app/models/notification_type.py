from sqlalchemy import Column, Integer, String, Text, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class NotificationType(Base):
    __tablename__ = "notification_types"

    id = Column(Integer, primary_key=True)
    notification_name = Column(String)

    notifications = relationship("SystemNotification", back_populates="notification_type")
