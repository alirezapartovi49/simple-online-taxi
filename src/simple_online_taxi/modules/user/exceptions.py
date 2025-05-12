from fastapi.exceptions import HTTPException
from starlette import status


class BaseException(HTTPException):
    def __init__(
        self, message: str, status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    ):
        self.message = message
        self.status_code = status_code
        super().__init__(self.status_code, self.message)


class UserNotFoundException(BaseException):
    def __init__(
        self,
        message: str = "user with given id not found",
        status_code: int = status.HTTP_404_NOT_FOUND,
    ):
        super().__init__(message, status_code)


class UserValidationException(BaseException):
    def __init__(
        self,
        message: str = "could not validate given data",
        status_code: int = status.HTTP_400_BAD_REQUEST,
    ):
        super().__init__(message, status_code)


class UserIntegrityException(BaseException):
    def __init__(
        self,
        message: str = "given data is duplicate",
        status_code: int = status.HTTP_409_CONFLICT,
    ):
        super().__init__(message, status_code)
