from fastapi import FastAPI
from .routers import entries
from .database import engine, Base

app = FastAPI(title="Ежедневник API")
Base.metadata.create_all(bind=engine)

app.include_router(entries.router)
