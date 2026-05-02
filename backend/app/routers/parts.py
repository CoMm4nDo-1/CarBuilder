from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from ..database import get_db
from ..models import Part, PriceHistory
from ..services.compatibility import compatible_parts_query
router=APIRouter(prefix='/parts',tags=['parts'])
@router.get('')
def list_parts(car_id:int|None=None,category:str|None=None,db:Session=Depends(get_db)):
    if car_id: return db.scalars(compatible_parts_query(db,car_id,category)).all()
    q=select(Part)
    return db.scalars(q).all()
@router.get('/featured')
def featured(db:Session=Depends(get_db)): return db.scalars(select(Part).where(Part.is_featured==True)).all()
@router.get('/sponsored')
def sponsored(db:Session=Depends(get_db)): return db.scalars(select(Part).where(Part.is_sponsored==True)).all()
@router.get('/{part_id}')
def part(part_id:int,db:Session=Depends(get_db)):
    p=db.get(Part,part_id)
    if not p: raise HTTPException(404,'Part not found')
    return p
@router.get('/{part_id}/price-history')
def ph(part_id:int,db:Session=Depends(get_db)): return db.scalars(select(PriceHistory).where(PriceHistory.part_id==part_id)).all()
