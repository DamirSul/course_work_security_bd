from pydantic import BaseModel
from datetime import date



class ResourceBase(BaseModel):
    resource_name: str
    quantity_available: int

class ResourceCreate(ResourceBase):
    pass

class Resource(ResourceBase):
    id: int

    class Config:
        orm_mode = True

class ResourceOut(ResourceBase):
    id: int

    class Config:
        orm_mode = True