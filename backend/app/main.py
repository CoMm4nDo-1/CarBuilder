from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select
from .database import init_db, get_session
from .models import Car, PartCategory, Part, BuildListItem
from .schemas import BuildListItemCreate

app = FastAPI(title='CarBuilder API')
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*'])

@app.on_event('startup')
def startup():
    init_db()

@app.get('/cars')
def get_cars(session: Session = Depends(get_session)):
    return session.exec(select(Car)).all()

@app.get('/cars/{car_id}')
def get_car(car_id: int, session: Session = Depends(get_session)):
    car = session.get(Car, car_id)
    if not car:
        raise HTTPException(404, 'Car not found')
    return car

@app.get('/categories')
def get_categories(session: Session = Depends(get_session)):
    return session.exec(select(PartCategory)).all()

@app.get('/parts')
def get_parts(car_id: int, category: str | None = None, session: Session = Depends(get_session)):
    if not session.get(Car, car_id):
        raise HTTPException(404, 'Car not found')
    q = select(Part)
    if category:
        q = q.where(Part.category == category)
    parts = session.exec(q).all()
    return [{**p.model_dump(), 'tags': p.tags.split(',')} for p in parts]

@app.get('/parts/{part_id}')
def get_part(part_id: int, session: Session = Depends(get_session)):
    p = session.get(Part, part_id)
    if not p:
        raise HTTPException(404, 'Part not found')
    return {**p.model_dump(), 'tags': p.tags.split(',')}

@app.get('/build-list')
def get_build_list(session: Session = Depends(get_session)):
    items = session.exec(select(BuildListItem)).all()
    rows=[]; total=0
    for i in items:
        part = session.get(Part, i.part_id)
        if not part:
            continue
        total += part.price
        rows.append({'item_id': i.id, 'part': {**part.model_dump(), 'tags': part.tags.split(',')}})
    return {'items': rows, 'total_cost': round(total,2)}

@app.post('/build-list/items')
def add_build_item(payload: BuildListItemCreate, session: Session = Depends(get_session)):
    if not session.get(Part, payload.part_id):
        raise HTTPException(404, 'Part not found')
    item = BuildListItem(part_id=payload.part_id)
    session.add(item); session.commit(); session.refresh(item)
    return {'id': item.id, 'part_id': item.part_id}

@app.delete('/build-list/items/{item_id}')
def del_item(item_id: int, session: Session = Depends(get_session)):
    item = session.get(BuildListItem, item_id)
    if not item:
        raise HTTPException(404, 'Item not found')
    session.delete(item); session.commit()
    return {'ok': True}

@app.delete('/build-list/clear')
def clear_list(session: Session = Depends(get_session)):
    for i in session.exec(select(BuildListItem)).all():
        session.delete(i)
    session.commit()
    return {'ok': True}
