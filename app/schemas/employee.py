from pydantic import BaseModel
from datetime import date

class EmployeeBase(BaseModel):
    full_name: str
    position: str
    phone_number: str

    class Config:
        orm_mode = True

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True

class EmployeeOut(EmployeeBase):
    id: int

    class Config:
        orm_mode = True

