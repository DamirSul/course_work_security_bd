# app/endpoints/plantings.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.models import FlowerPlanting
from app.schemas.flower_plantings import FlowerPlantingOut, FlowerPlantingCreate
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=FlowerPlantingOut)
def plant_flower(data: FlowerPlantingCreate, db: Session = Depends(get_db)):
    record = FlowerPlanting(**data.dict())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

@router.get("/summary", response_model=List[dict])
def get_summary(db: Session = Depends(get_db)):
    return db.query(FlowerPlanting).all()
