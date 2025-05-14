# app/endpoints/plantings.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.models import FlowerBase
from app.schemas.flower_base import FlowerBaseRead, FlowerBaseCreate
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=FlowerBaseRead)
def plant_flower(data: FlowerBaseCreate, db: Session = Depends(get_db)):
    record = FlowerBaseCreate(**data.dict())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

@router.get("/", response_model=List[FlowerBaseRead])
def get_summary(db: Session = Depends(get_db)):
    return db.query(FlowerBase).all()