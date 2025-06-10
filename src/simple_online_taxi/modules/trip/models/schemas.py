from pydantic import BaseModel, PositiveInt


class TripBase(BaseModel):
    driver_id: PositiveInt
    passenger_id: PositiveInt
    fare: float
    from_address: str
    to_address: str


class TripCreate(TripBase):
    passenger_id: int | None = None


class TripDataOutput(TripBase):
    id: PositiveInt

    class Config:
        from_attributes = True


TripDataOutput.model_rebuild()
