# app/endpoints/purchase_plan.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.purchase_plan import PurchasePlanCreate, PurchasePlanOut
from app.models import PurchasePlan as PurchasePlanModel

router = APIRouter()

@router.get("/pending", response_model=List[PurchasePlanOut])
def list_pending_plans(db: Session = Depends(get_db)):
    return db.query(PurchasePlanModel).all()

@router.post("/", response_model=PurchasePlanOut)
def create_purchase_plan(data: PurchasePlanCreate, db: Session = Depends(get_db)):
    plan = PurchasePlanModel(**data.dict())
    db.add(plan)
    db.commit()
    db.refresh(plan)
    return plan
