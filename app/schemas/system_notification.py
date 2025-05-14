from pydantic import BaseModel




class SystemNotificationBase(BaseModel):
    notification_type_id: int
    report_id: int
    from_employee_id: int
    to_employee_id: int
    notification_note: str

class SystemNotificationCreate(SystemNotificationBase):
    pass

class SystemNotification(SystemNotificationBase):
    id: int

    class Config:
        orm_mode = True