from datetime import timedelta
from typing import Annotated
import json

from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, Depends
from starlette import status

from .models import UserCreateOrUpdateInput, UserDataOutput, UserTokenData, User
from .auth import authenticate_user, create_access_token, bcrypt_context
from ...valkey import get_valkey_client, Valkey
from .respository import create_user
from .utils import get_request_user
from . import exceptions
from ...db import get_db


router = APIRouter(prefix="/user", tags=["user"])


@router.get("/me", response_model=UserDataOutput)
async def get_self(
    user: User = Depends(get_request_user), db: AsyncSession = Depends(get_db)
):
    return user


@router.post("/auth/register", status_code=status.HTTP_201_CREATED)
async def register_user(
    user_data: UserCreateOrUpdateInput,
    db: AsyncSession = Depends(get_db),
    valkey: Valkey = Depends(get_valkey_client),
) -> UserDataOutput:
    user_data = json.loads(user_data.model_dump_json())
    user_data["password"] = bcrypt_context.hash(user_data["password"])
    try:
        user = await create_user(db, user_data)
    except IntegrityError:
        raise exceptions.UserIntegrityException()
    user_cache_data = {"email": user.email, "id": user.id, "username": user.username}
    await valkey.set(f"registered_user:{user.id}", UserDataOutput(**user_cache_data).model_dump_json())
    return user


@router.post("/auth/login", response_model=UserTokenData)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: AsyncSession = Depends(get_db),
):
    user = await authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise exceptions.UserValidationException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    token = await create_access_token(user.username, user.id, timedelta(minutes=15))
    return {"access_token": token, "token_type": "bearer"}
