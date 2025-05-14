from pydantic import BaseModel
from datetime import date




class CareBase(BaseModel):
    care_name: str

class CareCreate(CareBase):
    pass

class Care(CareBase):
    id: int

    class Config:
        orm_mode = True