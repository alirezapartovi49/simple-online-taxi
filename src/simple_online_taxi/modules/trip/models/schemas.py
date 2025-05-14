from pydantic import BaseModel, PositiveInt

from ...user.models import DriverDataOutput, UserDataOutput


class TripBase(BaseModel):
    driver_id: PositiveInt
    passenger_id: PositiveInt
    fare: float


class TripCreate(TripBase):
    pass


class TripDataOutput(TripBase):
    id: PositiveInt
    driver: DriverDataOutput
    passenger: UserDataOutput

    class Config:
        from_attributes = True


TripDataOutput.model_rebuild()
