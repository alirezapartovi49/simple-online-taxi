import logging

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

from .modules import register_models
from .settings import settings


SQLALCHEMY_DATABASE_URL = settings.db_url

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    future=True,
    echo=False
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
)

Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

register_models()
