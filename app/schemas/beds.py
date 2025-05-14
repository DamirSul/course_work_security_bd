from pydantic import BaseModel
from datetime import date


class BedBase(BaseModel):
    bed_name: str
    total_capacity: int

class BedCreate(BedBase):
    pass

class Bed(BedBase):
    id: int
    current_occupancy: int

    class Config:
        orm_mode = True
