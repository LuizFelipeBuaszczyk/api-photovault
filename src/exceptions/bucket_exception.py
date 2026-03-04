from exceptions.exceptions import AppException
from fastapi import status

class BucketAlreadyExists(AppException):
    default_status_code = status.HTTP_409_CONFLICT
    default_detail = "Bucket already exists"