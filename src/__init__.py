from fastapi import Request, status
from fastapi.responses import JSONResponse
from exceptions.bucket_exception import BucketNotFound

async def bucket_not_found_exception_handler(request: Request, exc: BucketNotFound):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": exc.default_detail}
    )