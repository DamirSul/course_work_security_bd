# app/endpoints/auth.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.auth import EmployeeAuth
from app.schemas.auth import LoginRequest
from app.database import get_db

router = APIRouter()

@router.post("/login")
def login(code_data: LoginRequest, db: Session = Depends(get_db)):
    auth = db.query(EmployeeAuth).filter_by(access_code=code_data.code).first()
    if not auth:
        raise HTTPException(status_code=401, detail="Invalid access code")
    return {
        "id": auth.employee.id,
        "full_name": auth.employee.full_name,
        "role": auth.role
    }