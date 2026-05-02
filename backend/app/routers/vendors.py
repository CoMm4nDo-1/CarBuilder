from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from ..database import get_db
from ..models import Vendor
router=APIRouter(prefix='/vendors',tags=['vendors'])
@router.get('')
def list_vendors(db:Session=Depends(get_db)): return db.scalars(select(Vendor)).all()
@router.get('/{vendor_id}')
def get_vendor(vendor_id:int,db:Session=Depends(get_db)):
 v=db.get(Vendor,vendor_id)
 if not v: raise HTTPException(404,'Vendor not found')
 return v
