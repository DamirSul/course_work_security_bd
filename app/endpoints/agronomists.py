# app/endpoints/beds.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.employee import EmployeeOut
from app.models.agronomists import Agronomist

router = APIRouter()


@router.get("/", response_model=List[EmployeeOut])
def list_agronomists(db: Session = Depends(get_db)):
    agronomists = db.query(Agronomist).all()
    return [a.employee for a in agronomists]
