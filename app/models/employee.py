from sqlalchemy import Column, Integer, String, Text, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

from sqlalchemy.ext.hybrid import hybrid_property
from app.utils import encrypt_text, decrypt_text

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    position = Column(String)
    _phone_number = Column("phone_number", String)

    agronomist = relationship("Agronomist", back_populates="employee", uselist=False)
    purchase_plans = relationship("PurchasePlan", back_populates="employee")
    sent_notifications = relationship("SystemNotification", foreign_keys="[SystemNotification.from_employee_id]", back_populates="from_employee")
    received_notifications = relationship("SystemNotification", foreign_keys="[SystemNotification.to_employee_id]", back_populates="to_employee")
    auth = relationship("EmployeeAuth", back_populates="employee", uselist=False)

    @hybrid_property
    def phone_number(self):
        try:
            return decrypt_text(self._phone_number) if self._phone_number else ""
        except Exception:
            return "[ошибка дешифровки]"

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = encrypt_text(value)