from pydantic import BaseModel
from datetime import date




class BedBase(BaseModel):
    bed_name: str
    total_capacity: int
    current_occupancy: int

class BedCreate(BedBase):
    pass

class Bed(BedBase):
    id: int

    class Config:
        orm_mode = True