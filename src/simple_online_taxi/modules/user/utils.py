import json

from jose import ExpiredSignatureError
from starlette import status
from fastapi import Depends
from valkey import Valkey

from .auth import oauth2_bearer, decode_jwt
from .models.schemas import UserDataOutput
from ...valkey import get_valkey_client
from ...db import get_db, AsyncSession
from .respository import get_user
from . import exceptions


async def get_user_data(valkey: Valkey, db: AsyncSession, user_id: int):
    user_data = await valkey.get(f"registered_user:{user_id}")
    if user_data is None:
        user = await get_user(db, user_id)
        if user is None:
            raise exceptions.UserValidationException(
                status_code=status.HTTP_401_UNAUTHORIZED
            )
        user_data: UserDataOutput = UserDataOutput(**user)
        res = await valkey.set(
            f"registered_user:{user_data.id}", user_data.model_dump_json()
        )
        if res.decode() != "OK":
            raise exceptions.BaseException("error aucord in save data to cache")
    else:
        print("readed user from cache", user_id)
        if type(user_data) is bytes:
            user_data = user_data.decode()
        user_data: UserDataOutput = UserDataOutput(**json.loads(user_data))

    return user_data


async def get_request_user(
    token: str = Depends(oauth2_bearer),
    valkey: Valkey = Depends(get_valkey_client),
    db: AsyncSession = Depends(get_db),
):
    try:
        username, user_id = decode_jwt(token)
        if username is None or user_id is None:
            print("token username id failed")
            raise exceptions.UserValidationException(
                status_code=status.HTTP_401_UNAUTHORIZED
            )

        user_data = await get_user_data(valkey, db, user_id)
        print(user_data, username)
        if user_data.username != username:
            raise exceptions.UserValidationException(
                status_code=status.HTTP_401_UNAUTHORIZED
            )
        return user_data
    except ExpiredSignatureError:
        raise exceptions.UserValidationException(
            message="token expired", status_code=status.HTTP_401_UNAUTHORIZED
        )
