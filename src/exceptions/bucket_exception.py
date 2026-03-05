from exceptions.exceptions import AppException

class BucketAlreadyExists(AppException):
    default_status_code = 409
    default_detail = "Bucket already exists"
    
class BucketNotFound(AppException):
    default_status_code = 404
    default_detail = "Bucket not found"