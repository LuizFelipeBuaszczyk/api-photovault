from fastapi import status
from fastapi.responses import JSONResponse
from dto.buckets import request, response

from exceptions.exceptions import AppException
from services.bucket_service import BucketService

class BucketController:
    
    @staticmethod
    async def create_bucket(body: request.CreateBucketRequest) -> JSONResponse:
        
        await BucketService.create_bucket(body.name)
        
        created_bucket = response.GetBucketResponse(name=body.name)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=created_bucket.model_dump()
        )
        