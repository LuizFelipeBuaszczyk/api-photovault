from fastapi import APIRouter

from .buckets_objects import router as object_router
from .buckets import router as bucket_router

api_router = APIRouter()
api_router.include_router(object_router)
api_router.include_router(bucket_router)