# app/endpoints/beds.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.models import Bed, BedAction
from app.database import get_db

router = APIRouter()

@router.get("/", response_model=List[dict])
def list_beds(db: Session = Depends(get_db)):
    return db.query(Bed).all()

@router.get("/actions")
def get_bed_actions(db: Session = Depends(get_db)):
    return db.query(BedAction).all()
