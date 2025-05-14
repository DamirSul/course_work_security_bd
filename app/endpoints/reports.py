# app/endpoints/reports.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()

@router.get("/summary")
def get_report(db: Session = Depends(get_db)):
    return {"message": "Отчет по предприятию сформирован"}