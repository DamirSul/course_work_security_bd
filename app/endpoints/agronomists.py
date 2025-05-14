# app/endpoints/agronomists.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.employee import EmployeeOut
from app.schemas.agronomists import AgronomistCreate, Agronomist
from app.models.agronomists import Agronomist as AgronomistModel
from app.models import Employee

router = APIRouter()

@router.get("/", response_model=List[EmployeeOut])
def list_agronomists(db: Session = Depends(get_db)):
    agronomists = db.query(AgronomistModel).all()
    return [a.employee for a in agronomists]

@router.post("/", response_model=Agronomist)
def create_agronomist(data: AgronomistCreate, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == data.employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Сотрудник не найден")
    agronomist = AgronomistModel(employee_id=data.employee_id)
    db.add(agronomist)
    db.commit()
    db.refresh(agronomist)
    return agronomist