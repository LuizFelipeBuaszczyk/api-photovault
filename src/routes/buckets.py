from fastapi import APIRouter
from dto.buckets import request
from dto.buckets import response

from controller.bucket_controller import BucketController

router = APIRouter(
    prefix="/buckets",
    tags=["Buckets"]
)

@router.post("/", response_model=response.GetBucketResponse)
async def create_bucket(body: request.CreateBucketRequest):
    return await BucketController.create_bucket(body)