from logging import getLogger
from typing import Tuple
import asyncio

from valkey.asyncio import (
    Valkey,
    ConnectionError,
    ResponseError,
    AuthenticationError,
    TimeoutError,
)
from valkey import asyncio as valkey

from .settings import settings


Logger = getLogger("uvicorn.error")


async def create_client(
    valkey_node: Tuple[str, int] = (settings.valkey_host, settings.valkey_porst),
) -> Valkey:
    client = valkey.Valkey(host=valkey_node[0], port=valkey_node[1])
    return client


async def get_valkey_client():
    try:
        client = await create_client()
        yield client
    except asyncio.CancelledError:
        raise
    except AuthenticationError as e:
        Logger.error(
            f"Authentication error encountered: {e}",
        )
        raise e
    except TimeoutError as e:
        Logger.log(f"TimeoutError encountered: {e}")
        raise e
    except ConnectionError as e:
        Logger.error("ConnectionError encountered: {e}")
        raise e
    except ResponseError as e:
        Logger.error(f"RequestError encountered: {e}")
        raise e
    except Exception as e:
        Logger.error(f"Unexpected error: {e}")
        raise e
    finally:
        try:
            await client.close()
        except Exception as e:
            Logger.warning(
                f"Encountered an error while closing the client: {e}",
            )


async def test_valkey_connection():
    async with get_valkey_client() as client:
        if not await client.ping():
            raise Exception("error aucord")
