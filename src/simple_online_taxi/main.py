from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI, APIRouter

from .modules.user.routes import router as user_router
from .valkey import test_valkey_connection
from .settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    await test_valkey_connection()
    # await test_db_connection()
    yield


api_router = APIRouter(prefix="/api/v1")
api_router.include_router(user_router)

app = FastAPI(title="taxi online", debug=settings.debug, openapi_prefix="/api")
app.include_router(api_router)

if app.debug:
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)


@api_router.get("/", include_in_schema=False)
async def root():
    return "hello world!"
