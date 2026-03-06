from fastapi import APIRouter, status, UploadFile, File, Form
from fastapi.responses import JSONResponse

from controller.object_controller import ObjectController

router = APIRouter(
    prefix="/buckets/{bucket_name}/objects",
    tags=["Buckets / Objects"]
)

@router.get("/{object_name}")
async def get_object(bucket_name: str, object_name: str):
    return await ObjectController.get_object(bucket_name, object_name)

@router.post("/")
async def upload_object(
    bucket_name: str,
    file: UploadFile = File(...),
    object_name: str = Form(...)
):
    return await ObjectController.upload_object(file, bucket_name, object_name)