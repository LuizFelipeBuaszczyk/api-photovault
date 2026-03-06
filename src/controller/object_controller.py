from fastapi import status, UploadFile
from fastapi.responses import JSONResponse
from minio.helpers import ObjectWriteResult

from dto.objects import response
from services.object_service import ObjectService
from model.object_model import ObjectModel
from exceptions.exceptions import AppException


class ObjectController:
    
    @staticmethod
    async def get_object(bucket_name: str, object_name: str) -> JSONResponse:        
        object_url = await ObjectService.get_object_by_name(bucket_name, object_name)
                
        object_response = response.GetObjectResponse(url=object_url)
        
        return JSONResponse(
            status_code=status.HTTP_200_OK, 
            content=object_response.model_dump()
        )
        
    @staticmethod
    async def upload_object(file: UploadFile, bucket_name: str, object_name: str) -> JSONResponse:
        data = ObjectModel(
            bucket_name=bucket_name,
            object_name=object_name,
            file_bytes=file.file,
            content_type=file.content_type
        )
        created_object: ObjectWriteResult = await ObjectService.create_object(data)
        
        created_object_response = response.CreateObjectResponse(
            name=created_object.object_name,
            bucket_name=created_object.bucket_name,
            version_id=created_object.version_id
        )
        
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=created_object_response.model_dump()
        )
    