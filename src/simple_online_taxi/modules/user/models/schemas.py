from pydantic import BaseModel, PositiveInt, EmailStr, SecretStr, field_serializer


class UserCreateOrUpdateInput(BaseModel):
    email: EmailStr
    password: SecretStr
    username: str

    @field_serializer("password", when_used="json")
    def dump_secret(self, v):
        password = v.get_secret_value()
        return password


class UserDataOutput(BaseModel):
    id: PositiveInt
    email: EmailStr
    username: str


class UserTokenData(BaseModel):
    access_token: str
    token_type: str
