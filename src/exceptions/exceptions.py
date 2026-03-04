from fastapi.exceptions import HTTPException
from fastapi import status

class AppException(HTTPException):
    default_status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "Internal Server Error"

    def __init__(self, detail: str | None = None):
        super().__init__(
            status_code=self.default_status_code,
            detail=detail or self.default_detail
        )