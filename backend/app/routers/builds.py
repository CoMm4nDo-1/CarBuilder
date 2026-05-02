from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from ..database import get_db
from ..models import Build, BuildItem, Part
from ..schemas import BuildCreate, BuildItemCreate
router=APIRouter(prefix='/builds',tags=['builds'])

def refresh_total(db,b):
 items=db.scalars(select(BuildItem).where(BuildItem.build_id==b.id)).all(); b.total_price_cached=round(sum(i.price_at_time_added*i.quantity for i in items),2); db.commit(); db.refresh(b)

@router.get('')
def list_builds(db:Session=Depends(get_db)): return db.scalars(select(Build)).all()
@router.post('')
def create_build(payload:BuildCreate,db:Session=Depends(get_db)):
    b=Build(title=payload.title,car_id=payload.car_id,description=payload.description); db.add(b); db.commit(); db.refresh(b); return b
@router.get('/share/{share_slug}')
def share(share_slug:str,db:Session=Depends(get_db)): return db.scalar(select(Build).where(Build.share_slug==share_slug))
@router.get('/{build_id}')
def get_build(build_id:int,db:Session=Depends(get_db)):
 b=db.get(Build,build_id)
 if not b: raise HTTPException(404,'Build not found')
 items=db.scalars(select(BuildItem).where(BuildItem.build_id==build_id)).all(); return {'build':b,'items':items}
@router.put('/{build_id}')
def update(build_id:int,payload:BuildCreate,db:Session=Depends(get_db)):
 b=db.get(Build,build_id); b.title=payload.title; b.description=payload.description; db.commit(); return b
@router.delete('/{build_id}')
def delete(build_id:int,db:Session=Depends(get_db)):
 b=db.get(Build,build_id); db.delete(b); db.commit(); return {'ok':True}
@router.post('/{build_id}/items')
def add(build_id:int,payload:BuildItemCreate,db:Session=Depends(get_db)):
 p=db.get(Part,payload.part_id); i=BuildItem(build_id=build_id,part_id=payload.part_id,quantity=payload.quantity,price_at_time_added=p.current_price); db.add(i); db.commit(); b=db.get(Build,build_id); refresh_total(db,b); return i
@router.delete('/{build_id}/items/{item_id}')
def remove(build_id:int,item_id:int,db:Session=Depends(get_db)):
 i=db.get(BuildItem,item_id); db.delete(i); db.commit(); b=db.get(Build,build_id); refresh_total(db,b); return {'ok':True}
@router.delete('/{build_id}/clear')
def clear(build_id:int,db:Session=Depends(get_db)):
 for i in db.scalars(select(BuildItem).where(BuildItem.build_id==build_id)).all(): db.delete(i)
 db.commit(); b=db.get(Build,build_id); refresh_total(db,b); return {'ok':True}
