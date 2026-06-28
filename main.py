from fastapi import FastAPI
from db.database import engine, Base
from api.v1 import auth_router, admin_router

app = FastAPI(title="Shopla Express Courier API - Enterprise Edition")

@app.on_event("startup")
async def on_startup():
    # Database tables are now managed by Alembic migrations
    pass

app.include_router(auth_router.router)
app.include_router(admin_router.router)

@app.get("/")
def root():
    return {"message": "Welcome to Shopla Express API (Clean Architecture)"}
