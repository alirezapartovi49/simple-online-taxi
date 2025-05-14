from enum import Enum

from pydantic import BaseModel, PositiveInt, EmailStr, SecretStr, field_serializer
from typing import Optional


class DriverStatus(str, Enum):
    active = "active"
    inactive = "inactive"


class UserBase(BaseModel):
    email: EmailStr
    username: str


class UserCreateOrUpdateInput(UserBase):
    password: SecretStr

    @field_serializer("password", when_used="json")
    def dump_secret(self, v):
        return v.get_secret_value()


class UserDataOutput(UserBase):
    id: PositiveInt
    driver: Optional["DriverDataOutput"] = None

    class Config:
        from_attributes = True


class DriverCreateOrUpdate(BaseModel):
    license_number: str
    status: DriverStatus = DriverStatus.active


class DriverDataOutput(DriverCreateOrUpdate):
    id: PositiveInt
    user_id: PositiveInt

    class Config:
        from_attributes = True


UserDataOutput.model_rebuild()
