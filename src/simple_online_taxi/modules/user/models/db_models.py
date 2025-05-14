from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship

from .schemas import DriverStatus
from ....db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

    driver = relationship("Driver", back_populates="user", uselist=False)
    trips_as_passenger = relationship("Trip", back_populates="passenger")


class Driver(Base):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    license_number = Column(String(50), unique=True)
    status = Column("driver_status", Enum(DriverStatus, default=DriverStatus.active))

    user = relationship("User", back_populates="driver")
    trips = relationship("Trip", back_populates="driver")
