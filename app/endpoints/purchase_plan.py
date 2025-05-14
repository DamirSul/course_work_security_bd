# app/endpoints/purchase_plan.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import models

router = APIRouter()

@router.get("/pending", response_model=List[dict])
def list_pending_plans(db: Session = Depends(get_db)):
    return db.query(models.PurchasePlan).filter_by().all()