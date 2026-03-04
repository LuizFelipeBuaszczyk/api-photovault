from repositories.minio_repository import MinioRepository 
from exceptions import bucket_exception as exc   

class BucketService:
    
    @classmethod
    def create_bucket(cls, bucket_name: str) -> None:
        if MinioRepository.exists_bucket(bucket_name):
            raise exc.BucketAlreadyExists()
        
        MinioRepository.create_bucket(bucket_name)
        return