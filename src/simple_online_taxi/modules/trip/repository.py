from typing import List

from sqlalchemy import select, Sequence
from fastapi import Depends

from ...db import AsyncSession, get_db
from .models import Trip


async def get_user_trip(
    user_id: int, trip_id, db: AsyncSession = Depends(get_db)
) -> Trip | None:
    result = await db.execute(
        select(Trip).filter(Trip.passenger_id == user_id, Trip.id == trip_id)
    )
    return result.scalars().first()


async def get_user_trips(
    user_id: int, db: AsyncSession = Depends(get_db)
) -> List[Sequence[Trip]] | List[None]:
    result = await db.execute(select(Trip).filter(Trip.passenger_id == user_id))
    return result.scalars().all()


async def create_trip(trip: Trip, db: AsyncSession = Depends(get_db)) -> Trip:
    db.add(trip)
    await db.commit()
    await db.refresh(trip)
    return trip
