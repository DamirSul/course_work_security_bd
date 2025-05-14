# app/endpoints/employee.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.models import Employee
from app.schemas.employee import EmployeeOut, EmployeeCreate
from app.database import get_db

router = APIRouter()

@router.get("/", response_model=List[EmployeeOut])
def get_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()

@router.post("/", response_model=EmployeeOut)
def create_employee(data: EmployeeCreate, db: Session = Depends(get_db)):
    emp = Employee(full_name=data.full_name, position=data.position)
    emp.phone_number = data.phone_number
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return emp
