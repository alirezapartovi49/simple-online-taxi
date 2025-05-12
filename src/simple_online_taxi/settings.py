from pydantic import Field

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    debug: bool = Field(False, alias="DEBUG")

    valkey_host: str = Field("valkey", alias="VALKEY_HOST")
    valkey_porst: int = Field(6379, alias="VALKEY_PORT")

    secret_key: str = Field("secret_key", alias="SECRET_KEY")
    hash_algorithm: str = Field("HS256", alias="HASH_ALGORITHM")

    db_url: str = Field("sqlite+aiosqlite:///db.sqlite3", alias="DATABASE_URL")


settings = Settings()
