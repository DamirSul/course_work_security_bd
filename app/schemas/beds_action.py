from pydantic import BaseModel
from datetime import date


class BedActionBase(BaseModel):
    care_id: int
    action_date: date
    labor_costs: float

class BedActionCreate(BedActionBase):
    pass

class BedAction(BedActionBase):
    id: int

    class Config:
        orm_mode = True