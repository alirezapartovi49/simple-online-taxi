from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .models import Driver
from .models import User


async def get_user(db: AsyncSession, user_id: int) -> User | None:
    result = await db.execute(select(User).filter(User.id == user_id))
    return result.scalars().first()


async def create_user(db: AsyncSession, user_data: Dict) -> User:
    user = User(**user_data)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def create_driver(db: AsyncSession, driver: Driver) -> Driver:
    db.add(driver)
    await db.commit()
    await db.refresh(driver)
    return driver


async def get_driver(db: AsyncSession, user_id: int) -> Driver | None:
    result = await db.execute(select(Driver).filter(user_id == user_id))
    return result.scalars().first()
