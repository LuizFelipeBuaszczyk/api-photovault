from fastapi import APIRouter

from .images import router as image_router
from .buckets import router as bucket_router

api_router = APIRouter()
api_router.include_router(image_router)
api_router.include_router(bucket_router)