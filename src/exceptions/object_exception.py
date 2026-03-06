from exceptions.exceptions import AppException

class ObjectNotFound(AppException):
    default_status_code = 404
    default_detail = "Object not found"