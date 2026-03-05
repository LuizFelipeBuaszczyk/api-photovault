

from model.object_model import ObjectModel
from minio.helpers import ObjectWriteResult

from repositories.minio_repository import MinioRepository
from exceptions.bucket_exception  import BucketNotFound


class ObjectService:
    
    @classmethod
    async def create_object(cls, object: ObjectModel) -> ObjectWriteResult:
        
        if not MinioRepository.exists_bucket(object.bucket_name):
            raise BucketNotFound()
        
        object.file_bytes.seek(0, 2)
        object.length = object.file_bytes.tell()
        object.file_bytes.seek(0, 0)
        
        return MinioRepository.create_object_bytes(object)