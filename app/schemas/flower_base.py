from pydantic import BaseModel
from datetime import date



class FlowerBase(BaseModel):
    flower_name: str
    variety: str
    color: str
    description: str

class FlowerBaseCreate(FlowerBase):
    pass

class FlowerBaseRead(FlowerBase):
    id: int

    class Config:
        orm_mode = True