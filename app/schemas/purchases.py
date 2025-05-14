from pydantic import BaseModel
from datetime import date



class PurchaseBase(BaseModel):
    purchase_plan_id: int
    create_date: date

class PurchaseCreate(PurchaseBase):
    pass

class Purchase(PurchaseBase):
    id: int

    class Config:
        orm_mode = True

class PurchaseOut(PurchaseBase):
    id: int

    class Config:
        orm_mode = True