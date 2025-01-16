from fastapi import APIRouter, UploadFile, File, Request
import os
import shutil
from fastapi import APIRouter, UploadFile, File, Request, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from backend.src.feature.directories.file_utils import folderCompare, get_size, diff
import tempfile
from zipfile import ZipFile

router = APIRouter()

home_path = "/your/home/path"  # Define your home path

@router.post("/load-data")
async def loaddata(request: Request):
    data = await request.json()
    name = data['name']
    folder = data['folder']
    curr_path = os.path.join(home_path, folder, name)
    folders = []
    folders_date = []
    files = []
    files_size = []
    files_date = []
    if folderCompare(home_path, curr_path):
        dir_list = os.listdir(curr_path)
        for item in dir_list:
            if os.path.isdir(os.path.join(curr_path, item)):
                folders.append(item)
                folder_date = diff(os.path.join(curr_path, item))
                folders_date.append(folder_date)
        for item in dir_list:
            if os.path.isfile(os.path.join(curr_path, item)):
                files.append(item)
                file_size = get_size(os.path.join(curr_path, item))
                files_size.append(file_size)
                file_date = diff(os.path.join(curr_path, item))
                files_date.append(file_date)

        folders_data = list(zip(folders, folders_date))
        files_data = list(zip(files, files_size, files_date))

        return JSONResponse(content={"folders_data": folders_data, "files_data": files_data})
    else:
        raise HTTPException(status_code=201, detail="Folder comparison failed")

@router.get('/info')
async def info():
    foldername = os.path.basename(home_path)
    lastmd = diff(home_path)
    dir_list = os.listdir(home_path)
    file = 0
    folder = 0
    for item in dir_list:
        if os.path.isdir(item):
            folder += 1
        elif os.path.isfile(item):
            file += 1
    data = {'foldername': foldername, 'lastmd': lastmd, 'file': file, 'folder': folder}
    return JSONResponse(content=data)

@router.post('/folderlist')
async def folderlist(request: Request):
    data = await request.json()
    foldername = data['foldername']
    folder = data['folder']
    curr_path = os.path.join(home_path, folder, foldername)
    if folderCompare(home_path, curr_path) and str(curr_path) != (str(os.path.join(home_path, '..'))):
        dir_list = os.listdir(curr_path)
        folders = []
        for item in dir_list:
            if os.path.isdir(os.path.join(curr_path, item)):
                folders.append({"path": item})
        return JSONResponse(content={"item": folders})
    else:
        return JSONResponse(content={"item": "no more folder", "status": False})

@router.post('/copyItem')
async def copyItem(request: Request):
    data = await request.json()
    source = data['source']
    itemName = data['itemName']
    destination = data['destination']
    fodestination = data['fodestination']
    fullSource = os.path.join(home_path, source, itemName)
    fullDestination = os.path.join(home_path, source, fodestination, destination)
    try:
        shutil.copy2(fullSource, fullDestination)
        return "1"
    except NotADirectoryError:
        shutil.copytree(fullSource, fullDestination)
        return "1"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/moveItem')
async def moveItem(request: Request):
    data = await request.json()
    source = data['source']
    destination = data['destination']
    itemName = data['itemName']
    fodestination = data['fodestination']
    fullSource = os.path.join(home_path, source, itemName)
    fullDestination = os.path.join(home_path, source, fodestination, destination)
    try:
        shutil.move(fullSource, fullDestination)
        return "1"
    except NotADirectoryError:
        shutil.copytree(fullSource, fullDestination)
        return "1"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/new-folder")
async def newfolder(request: Request):
    data = await request.json()
    name = data['name']
    folder = data['folder']
    try:
        os.mkdir(os.path.join(home_path, folder, name))
        return "1"
    except IOError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/new-file")
async def newfile(request: Request):
    data = await request.json()
    name = data['name']
    folder = data['folder']
    file = os.path.join(home_path, folder, name)
    try:
        with open(file, 'w') as fp:
            pass
        return "1"
    except IOError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/upload")
async def upload(file: UploadFile = File(...), folder: str = Form(...)):
    target = os.path.join(home_path, folder)
    try:
        with open(os.path.join(target, file.filename), "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return "1"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/delete")
async def delete(request: Request):
    data = await request.json()
    name = data['name']
    folder = data['folder']
    target = os.path.join(home_path, folder, name)
    if os.path.isdir(target):
        folders = os.listdir(target)
        if folders == []:
            try:
                os.rmdir(target)
                return "1"
            except IOError as e:
                raise HTTPException(status_code=500, detail=str(e))
        else:
            try:
                shutil.rmtree(target)
                return "1"
            except IOError as e:
                raise HTTPException(status_code=500, detail=str(e))
    else:
        if os.path.isfile(target):
            try:
                os.remove(target)
                return "1"
            except IOError as e:
                raise HTTPException(status_code=500, detail=str(e))

@router.post("/rename")
async def rename(request: Request):
    data = await request.json()
    name = data['name']
    folder = data['folder']
    dst = data['dst']
    target = os.path.join(home_path, folder, name)
    fullDestination = os.path.join(home_path, folder, dst)
    try:
        os.rename(target, fullDestination)
        return "1"
    except IOError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/download/{name:path}")
async def download(name: str):
    target = os.path.join(home_path, name)
    def get_all_dir(directory):
        file_paths = list()
        for root, directories, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)
        return file_paths

    if os.path.isdir(target):
        os.chdir(os.path.dirname(target))
        foldername = os.path.basename(target)
        file_paths = get_all_dir(foldername)
        temp_dir = tempfile.gettempdir()
        zipname = os.path.join(temp_dir, foldername)

        try:
            with ZipFile(f"{foldername}.zip", "w") as zip:
                for file in file_paths:
                    zip.write(file)
            return FileResponse(path=f"{foldername}.zip", filename=f"{foldername}.zip", media_type='application/zip')

        finally:
            if os.path.exists(f"{foldername}.zip"):
                os.remove(f"{foldername}.zip")
    else:
        try:
            return FileResponse(path=target, filename=os.path.basename(target), media_type='application/octet-stream')
        except IOError:
            raise HTTPException(status_code=500, detail="Can't download")