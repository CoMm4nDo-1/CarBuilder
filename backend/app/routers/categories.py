from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from ..database import get_db
from ..models import PartCategory
router=APIRouter(prefix='/categories',tags=['categories'])
@router.get('')
def list_categories(db:Session=Depends(get_db)): return db.scalars(select(PartCategory).order_by(PartCategory.display_order)).all()
