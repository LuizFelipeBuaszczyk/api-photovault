from fastapi.responses import JSONResponse
from fastapi import Request

from exceptions.exceptions import AppException

async def app_exception_handler(request: Request, exc: Exception):
    app_exc = exc 
    
    if isinstance(app_exc, AppException):
        return JSONResponse(
            status_code=app_exc.status_code,
            content={"detail": app_exc.detail},
        )
    else:
        return JSONResponse(
            status_code=500,
            content={"detail": app_exc.args[0]},
        )
    
