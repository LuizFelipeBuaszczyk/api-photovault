from minio import Minio
from minio.helpers import ObjectWriteResult
from minio.datatypes import Object
from urllib3.response import BaseHTTPResponse

from utils import settings
from model.object_model import ObjectModel

class MinioRepository:
    _client = Minio(
        endpoint=settings.MINIO_ENDPOINT,
        access_key=settings.MINIO_ACCESS_KEY,
        secret_key=settings.MINIO_SECRET_KEY,
        secure=False if settings.DEBUG else True # Se for ambiente de desenvolvimento, usar http
    )
    
    
    @classmethod
    def exists_bucket(cls, bucket_name: str) -> bool:
        return cls._client.bucket_exists(bucket_name)
    
    @classmethod
    def create_bucket(cls, bucket_name: str) -> None:
        cls._client.make_bucket(bucket_name)
        
    @classmethod
    def delete_bucket(cls, bucket_name: str) -> None:
        cls._client.remove_bucket(bucket_name)
        
    @classmethod
    def create_object_bytes(cls, object: ObjectModel) -> ObjectWriteResult:
        return cls._client.put_object(
            bucket_name=object.bucket_name, 
            object_name=object.object_name, 
            data=object.file_bytes,
            length=object.length,
            content_type=object.content_type
            )
        
    @classmethod
    def create_object_file(cls, object: ObjectModel) -> ObjectWriteResult:
        return cls._client.fput_object(
            bucket_name=object.bucket_name, 
            object_name=object.object_name, 
            file_path=object.file_path
            )
    
    @classmethod
    def get_object_url(cls, bucket_name: str, object_name: str):
        return cls._client.presigned_get_object(bucket_name, object_name)
        
    @classmethod
    def exists_object(cls, bucket_name: str, object_name: str) -> Object:
        return cls._client.stat_object(bucket_name, object_name)
        
        