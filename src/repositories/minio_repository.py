from minio import Minio

from utils import settings

class MinioRepository:
    _client = Minio(
        endpoint=settings.MINIO_ENDPOINT,
        access_key=settings.MINIO_ACCESS_KEY,
        secret_key=settings.MINIO_SECRET_KEY,
        secure=False
    )
    
    @classmethod
    def exists_bucket(cls, bucket_name: str) -> bool:
        return cls._client.bucket_exists(bucket_name)
    
    @classmethod
    def create_bucket(cls, bucket_name: str) -> None:
        cls._client.make_bucket(bucket_name)
    