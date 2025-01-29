import os

from fastapi import FastAPI, File, UploadFile, APIRouter

from app.services import process_image
from fastapi.responses import JSONResponse

router = APIRouter()
UPLOAD_DIR = "uploads"


@router.post("/image_upload/", tags=["image_upload"])
async def read_users(file: UploadFile = File(...)):
    image_path = os.path.join(UPLOAD_DIR, file.filename)
    print(image_path)
    color_data = process_image(image_path, n_colors=3)
    return JSONResponse(content=color_data)

