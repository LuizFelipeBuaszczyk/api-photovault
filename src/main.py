from fastapi import FastAPI

from routes import api_router
from exceptions.handler import app_exception_handler
from exceptions.exceptions import AppException

app = FastAPI()
app.include_router(api_router)
app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(Exception, app_exception_handler)