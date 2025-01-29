from fastapi import FastAPI, File, UploadFile, APIRouter
from app.services import process_image
from fastapi.responses import JSONResponse
from PIL import Image
from io import BytesIO


router = APIRouter()
UPLOAD_DIR = "uploads"


@router.post("/image_upload/", tags=["image_upload"])
async def read_users(file: UploadFile = File(...)):
    image_data = await file.read()
    image = Image.open(BytesIO(image_data))
    color_data = process_image(image, n_colors=3)
    return JSONResponse(content=color_data)

