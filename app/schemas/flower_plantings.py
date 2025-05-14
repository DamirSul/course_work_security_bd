from pydantic import BaseModel
from datetime import date

class FlowerPlantingBase(BaseModel):
    flower_id: int
    bed_id: int
    action_id: int
    quantity_planted: int

class FlowerPlantingCreate(FlowerPlantingBase):
    pass

class FlowerPlanting(FlowerPlantingBase):
    id: int

    class Config:
        orm_mode = True


class FlowerPlantingOut(FlowerPlantingBase):
    id: int

    class Config:
        orm_mode = True