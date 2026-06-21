from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.infrastructure.mongo import MongoManager
from app.api.v1.health_routes import (router as health_router)

app = FastAPI(
    title="DirektAI Backend",
    version="1.0.0"
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    MongoManager.connect()
    yield
    MongoManager.disconnect()


app = FastAPI(
    title="DirektAI Backend",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(
    health_router,
    prefix="/api/v1",
    tags=["Health"]
)