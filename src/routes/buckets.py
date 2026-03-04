from fastapi import APIRouter
from dto.buckets import request
from dto.buckets import response

from controller.bucket_controller import BucketController

router = APIRouter(
    prefix="/buckets",
    tags=["Buckets"]
)

@router.post("/", response_model=response.GetBucketResponse)
def create_bucket(body: request.CreateBucketRequest):
    return BucketController.create_bucket(body)