from repositories.minio_repository import MinioRepository 
from exceptions.bucket_exception import BucketAlreadyExists   

class BucketService:
    
    @classmethod
    async def create_bucket(cls, bucket_name: str) -> None:
        if MinioRepository.exists_bucket(bucket_name):
            raise BucketAlreadyExists()
        
        MinioRepository.create_bucket(bucket_name)
        return