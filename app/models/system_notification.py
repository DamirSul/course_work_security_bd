from sqlalchemy import Column, Integer, String, Text, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class SystemNotification(Base):
    __tablename__ = "system_notifications"

    id = Column(Integer, primary_key=True)
    notification_type_id = Column(Integer, ForeignKey("notification_types.id"))
    report_id = Column(Integer, ForeignKey("reports.id"))
    from_employee_id = Column(Integer, ForeignKey("employees.id"))
    to_employee_id = Column(Integer, ForeignKey("employees.id"))
    notification_note = Column(Text)

    notification_type = relationship("NotificationType", back_populates="notifications")
    report = relationship("Report", back_populates="notifications")
    from_employee = relationship("Employee", foreign_keys=[from_employee_id], back_populates="sent_notifications")
    to_employee = relationship("Employee", foreign_keys=[to_employee_id], back_populates="received_notifications")