from fastapi import APIRouter, status, UploadFile, File, Form
from fastapi.responses import JSONResponse

from controller.object_controller import ObjectController

router = APIRouter(
    prefix="/objects",
    tags=["Objects"]
)

@router.post("/")
async def upload_object(
    file: UploadFile = File(...),
    bucket_name: str = Form(...),
    object_name: str = Form(...)
):
    return await ObjectController.upload_object(file, bucket_name, object_name)