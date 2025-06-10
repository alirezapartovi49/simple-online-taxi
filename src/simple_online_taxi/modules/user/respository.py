from typing import Dict, List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Sequence
from fastapi import Depends

from ...db import get_db

from .models import Driver
from .models import User


async def get_user(user_id: int, db: AsyncSession = Depends(get_db)) -> User | None:
    result = await db.execute(select(User).filter(User.id == user_id))
    return result.scalars().first()


async def create_user(user: User, db: AsyncSession = Depends(get_db)) -> User:
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def create_driver(driver: Driver, db: AsyncSession = Depends(get_db)) -> Driver:
    db.add(driver)
    await db.commit()
    await db.refresh(driver)
    return driver


async def get_driver(user_id: int, db: AsyncSession = Depends(get_db)) -> Driver | None:
    result = await db.execute(select(Driver).filter(Driver.user_id == user_id))
    return result.scalars().first()


async def get_all_drivers(
    db: AsyncSession = Depends(get_db),
) -> List[Sequence[Driver]] | List[None]:
    result = await db.execute(select(Driver).join(User, Driver.id == User.id))
    return result.scalars().all()
