from sqlalchemy import Column, Integer, ForeignKey, Numeric, String
from sqlalchemy.orm import relationship

from ....db import Base


class Trip(Base):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True)
    driver_id = Column(Integer, ForeignKey("drivers.id"))
    passenger_id = Column(Integer, ForeignKey("users.id"))
    fare = Column(Numeric(10, 2))
    from_address = Column(String(50))
    to_address = Column(String(50))

    driver = relationship("Driver", back_populates="trips")
    passenger = relationship("User", back_populates="trips_as_passenger")
