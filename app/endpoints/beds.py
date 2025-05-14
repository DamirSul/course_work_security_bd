from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.models import Bed, BedAction
from app.schemas.beds import BedCreate, Bed as BedSchema
from app.database import get_db

router = APIRouter()

@router.get("/", response_model=List[BedSchema])
def list_beds(db: Session = Depends(get_db)):
    return db.query(Bed).all()

@router.post("/", response_model=BedSchema)
def create_bed(data: BedCreate, db: Session = Depends(get_db)):
    bed = Bed(**data.dict(), current_occupancy=0)
    db.add(bed)
    db.commit()
    db.refresh(bed)
    return bed

@router.get("/actions")
def get_bed_actions(db: Session = Depends(get_db)):
    return db.query(BedAction).all()
