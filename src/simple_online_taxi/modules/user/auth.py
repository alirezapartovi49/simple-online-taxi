from typing import Annotated
import datetime

from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from sqlalchemy import select
from fastapi import Depends
from jose import jwt
import bcrypt

from .models.schemas import UserCreateOrUpdateInput
from .models.db_models import User
from ...settings import settings
from ...db import get_db


SECRET_KEY = settings.secret_key
ALGORITHM = settings.hash_algorithm
bcrypt.__about__ = bcrypt

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="api/v1/user/auth/login")


db_depnds = Annotated[AsyncSession, Depends(get_db)]


async def create_user(db: db_depnds, create_request: UserCreateOrUpdateInput):
    create_user_model = User(
        username=create_request.username,
        password=bcrypt_context.hash(create_request.password),
    )

    db.add(create_user_model)
    db.commit()


async def create_access_token(username, id, expire_time):
    payload = {
        "sub": str(username),
        "id": str(id),
        "exp": datetime.datetime.now(datetime.timezone.utc) + expire_time,
    }
    print(payload)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


async def authenticate_user(username: str, password: str, db: AsyncSession):
    result = await db.execute(select(User).where(User.username == username))
    user = result.scalar_one_or_none()
    if user is None:
        return False
    if not bcrypt_context.verify(password, user.password):
        return False
    return user


def decode_jwt(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    print(payload)
    username: str = payload.get("sub", None)
    user_id: int = payload.get("id", None)
    return username, user_id
