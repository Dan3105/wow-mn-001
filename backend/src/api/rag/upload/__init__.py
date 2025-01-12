from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
import os
import shutil

router = APIRouter()

class FileUploadResponse(BaseModel):
    filename: str
    content_type: str
    size: int
    dir: str

@router.post("/upload-file", response_model=FileUploadResponse)
async def upload_file(file: UploadFile = File(...)) -> FileUploadResponse:
    # Define the directory to save the uploaded file
    upload_dir = os.path.join(os.getenv('APPDATA', '/tmp'), 'uploads')
    os.makedirs(upload_dir, exist_ok=True)
    
    # Save the uploaded file
    file_path = os.path.join(upload_dir, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return FileUploadResponse(
        filename=file.filename,
        content_type=file.content_type,
        size=os.path.getsize(file_path),
        dir=file_path
    )