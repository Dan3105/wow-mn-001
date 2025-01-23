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

    norm_path = os.path.normpath(path)
    resource = DirectoryOperations(norm_path)

    return resource.list_directory()

@router.post("/upload")
def upload_file(parent_path: str = Form(...), file: UploadFile = File(...)):
    try:
        src = parent_path if parent_path else os.getenv("OS_PATH")
        file_name = file.filename
        file_path = os.path.join(src, file_name)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            return JSONResponse(content={"message": "File uploaded successfully"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/upload-files")
def upload_files(parent_path: str = Form(...), files: list[UploadFile] = File(...)):
    try:
        src = parent_path if parent_path else os.getenv("OS_PATH")
        uploaded_files = []

        for file in files:
            file_name = file.filename
            file_path = os.path.join(src, file_name)

            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
                uploaded_files.append(file_name)

        return JSONResponse(content={
            "message": "Files uploaded successfully",
            "uploaded_files": uploaded_files
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/create-directory")
def create_directory(folder: str = Form(...), name: str = Form(...)):
    try:
        src = os.getenv("OS_PATH")
        new_dir_path = os.path.join(src, folder, name)
        os.mkdir(new_dir_path)
        return JSONResponse(content={"message": "Directory created successfully"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.delete("/delete-file")
def delete(file_name: str = Form(...), curr_path: str = Form(...)):
    try:
        path = os.path.normpath(os.path.join(curr_path, file_name))
        if os.path.isfile(path):
            os.remove(path)
        else:
            raise HTTPException(status_code=400, detail="Invalid or non-existent file path")
        return JSONResponse(content={"message": "File deleted successfully"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/delete-directory")
def delete(curr_path: str = Form(...)):
    try:
        path = os.path.normpath(curr_path)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            raise HTTPException(status_code=400, detail="Invalid or non-existent directory path")
        return JSONResponse(content={"message": "File or directory deleted successfully"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))    

@router.post("/rename")
def rename(file_name: str = Form(...), dst: str = Form(...), curr_path: str = Form(...)):
    try:
        target = os.path.join(curr_path, file_name)
        full_destination = os.path.join(curr_path, dst)
        os.rename(target, full_destination)
        return JSONResponse(content={"message": "File or directory renamed successfully"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/move")
def move(src: str = Form(...), dst: str = Form(...)):
    try:
        target = os.path.normpath(src)
        full_destination = os.path.normpath(dst)
        shutil.move(target, full_destination)
        return JSONResponse(content={"message": "File or directory moved successfully"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# @router.post("/rename")
# async def rename(request: Request):
#     data = await request.json()
#     name = data['name']
#     folder = data['folder']
#     dst = data['dst']
#     target = os.path.join(home_path, folder, name)
#     fullDestination = os.path.join(home_path, folder, dst)
#     try:
#         os.rename(target, fullDestination)
#         return "1"
#     except IOError as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @router.get("/download/{name:path}")
# async def download(name: str):
#     target = os.path.join(home_path, name)
#     def get_all_dir(directory):
#         file_paths = list()
#         for root, directories, files in os.walk(directory):
#             for filename in files:
#                 filepath = os.path.join(root, filename)
#                 file_paths.append(filepath)
#         return file_paths

#     if os.path.isdir(target):
#         os.chdir(os.path.dirname(target))
#         foldername = os.path.basename(target)
#         file_paths = get_all_dir(foldername)
#         temp_dir = tempfile.gettempdir()
#         zipname = os.path.join(temp_dir, foldername)

#         try:
#             with ZipFile(f"{foldername}.zip", "w") as zip:
#                 for file in file_paths:
#                     zip.write(file)
#             return FileResponse(path=f"{foldername}.zip", filename=f"{foldername}.zip", media_type='application/zip')

#         finally:
#             if os.path.exists(f"{foldername}.zip"):
#                 os.remove(f"{foldername}.zip")
#     else:
#         try:
#             return FileResponse(path=target, filename=os.path.basename(target), media_type='application/octet-stream')
#         except IOError:
#             raise HTTPException(status_code=500, detail="Can't download")