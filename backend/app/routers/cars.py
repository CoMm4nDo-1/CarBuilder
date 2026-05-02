from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from ..database import get_db
from ..models import Car
router=APIRouter(prefix='/cars',tags=['cars'])
@router.get('')
def list_cars(db:Session=Depends(get_db)): return db.scalars(select(Car)).all()
@router.get('/{car_id}')
def get_car(car_id:int,db:Session=Depends(get_db)):
    c=db.get(Car,car_id)
    if not c: raise HTTPException(404,'Car not found')
    return c
