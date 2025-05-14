from pydantic import BaseModel
from datetime import date




class AgronomistBase(BaseModel):
    employee_id: int

class AgronomistCreate(AgronomistBase):
    pass

class Agronomist(AgronomistBase):
    id: int

    class Config:
        orm_mode = True