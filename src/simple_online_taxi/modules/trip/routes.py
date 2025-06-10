from typing import List

from fastapi import APIRouter, Depends

from ..user.utils import get_request_user
from ..user.models import UserDataOutput
from ...db import get_db, AsyncSession
from . import repository as repo
from . import models

router = APIRouter(prefix="/trip", tags=["trip"])


@router.post("/add-trip", response_model=models.TripDataOutput)
async def create_trip(
    trip_input: models.TripCreate,
    user: UserDataOutput = Depends(get_request_user),
    db: AsyncSession = Depends(get_db),
):
    trip_input.passenger_id = user.id
    trip = models.Trip(**trip_input.model_dump())
    trip = await repo.create_trip(trip, db)
    return trip


@router.post("/all", response_model=List[models.TripDataOutput])
async def user_trips(
    user: UserDataOutput = Depends(get_request_user),
    db: AsyncSession = Depends(get_db),
):
    trips_data = await repo.get_user_trips(user.id, db)
    return trips_data
