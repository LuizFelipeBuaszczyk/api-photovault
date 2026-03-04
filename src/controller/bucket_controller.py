from fastapi import status
from fastapi.responses import JSONResponse
from dto.buckets import request, response

from exceptions.exceptions import AppException
from service.bucket_service import BucketService

class BucketController:
    
    @staticmethod
    def create_bucket(body: request.CreateBucketRequest) -> JSONResponse:
        try:
            BucketService.create_bucket(body.name)
           
            created_bucket = response.GetBucketResponse(name=body.name)
            return JSONResponse(
                status_code=status.HTTP_201_CREATED,
                content=created_bucket.model_dump()
            )
        except Exception as e:
            # TODO: Deixar essa exceção genérica -- Implementar logging para exceções internas
            raise AppException(detail=str(e))