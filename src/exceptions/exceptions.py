class AppException(Exception):
    default_status_code = 500
    default_detail = "Internal Server Error"

    def __init__(
        self, 
        detail: str | None = None, 
        status_code: int | None = None
    ):
        self.status_code = (
            status_code if status_code is not None else self.default_status_code
        )

        self.detail = (
            detail if detail is not None else self.default_detail
        )
        