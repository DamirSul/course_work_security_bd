from pydantic import BaseModel
from datetime import date


class PurchasePlanBase(BaseModel):
    resource_id: int
    quantity: int
    employee_id: int
    create_date: date

class PurchasePlanCreate(PurchasePlanBase):
    pass

class PurchasePlan(PurchasePlanBase):
    id: int

    class Config:
        orm_mode = True

class PurchasePlanOut(PurchasePlanBase):
    id: int

    class Config:
        orm_mode = True
