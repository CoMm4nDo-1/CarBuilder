from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .seed import run_seed
from .routers import cars,categories,parts,builds,vendors,users,payments,admin

app=FastAPI(title='CarBuilder API')
app.add_middleware(CORSMiddleware,allow_origins=[settings.frontend_url,'*'],allow_methods=['*'],allow_headers=['*'])

@app.on_event('startup')
def startup(): run_seed()

for r in [cars.router,categories.router,parts.router,builds.router,vendors.router,users.router,payments.router,admin.router]:
    app.include_router(r)

@app.get('/')
def root(): return {'name':'CarBuilder API','status':'ok'}
