import os
import shutil
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from feature.directories.operations.directory_operations import DirectoryOperations

router = APIRouter()

@router.get("/{src:path}")
def list_directories(src: str = None):
    # Determine the path
    path = src if src else os.getenv("OS_PATH")

    if path is None or not os.path.isdir(path):
        print(f"Invalid or non-existent directory path: {path}")
        raise HTTPException(status_code=400, detail="Invalid or non-existent directory path")

    resource = DirectoryOperations(path)

    return resource.list_directory()

@router.post("/upload")
async def upload_file(parent_path: str = Form(...), file: UploadFile = File(...)):
    try:
        src = parent_path.path
        file_name = file.filename
        file_path = os.path.join(src, file_name)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            return JSONResponse(content={"message": "File uploaded successfully"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

