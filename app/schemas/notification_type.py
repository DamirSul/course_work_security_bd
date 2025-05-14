from pydantic import BaseModel



class NotificationTypeBase(BaseModel):
    notification_name: str

class NotificationTypeCreate(NotificationTypeBase):
    pass

class NotificationType(NotificationTypeBase):
    id: int

    class Config:
        orm_mode = True
