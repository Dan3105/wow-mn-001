from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from dbcontext.postgres import get_db
from feature.directories.dto.file_dto import FileCreateDto, FileUpdateDto, FileResponseDto
from feature.directories.dto.directory_dto import DirectoryCreateDto, DirectoryUpdateDto, DirectoryResponseDto
from feature.directories.file.file_commands import add_file, remove_file, update_file
from feature.directories.file.file_queries import get_files_by_directory_id, get_files_from_root
from feature.directories.directory.directory_commands import add_directory, remove_directory, update_directory
from feature.directories.directory.directory_queries import get_directories_by_parent_id, get_root_directories

router = APIRouter()

# File Endpoints
@router.post("/files/", response_model=FileResponseDto)
async def create_file(file_create_dto: FileCreateDto, db: Session = Depends(get_db)):
    return add_file(file_create_dto, db)

@router.delete("/files/{file_id}", response_model=bool)
async def delete_file(file_id: int, db: Session = Depends(get_db)):
    return remove_file(file_id, db)

@router.put("/files/{file_id}", response_model=FileResponseDto)
async def edit_file(file_id: int, file_update_dto: FileUpdateDto, db: Session = Depends(get_db)):
    updated_file = update_file(file_id, file_update_dto, db)
    if not updated_file:
        raise HTTPException(status_code=404, detail="File not found")
    return updated_file

@router.get("/files/directory/{directory_id}", response_model=List[FileResponseDto])
async def list_files_by_directory(directory_id: int, db: Session = Depends(get_db)):
    return get_files_by_directory_id(directory_id, db)

@router.get("/files/root", response_model=List[FileResponseDto])
async def list_files_from_root(db: Session = Depends(get_db)):
    return get_files_from_root(db)

# Directory Endpoints
@router.post("/directories/", response_model=DirectoryResponseDto)
async def create_directory(directory_create_dto: DirectoryCreateDto, db: Session = Depends(get_db)):
    return add_directory(directory_create_dto, db)

@router.delete("/directories/{directory_id}", response_model=bool)
async def delete_directory(directory_id: int, db: Session = Depends(get_db)):
    return remove_directory(directory_id, db)

@router.put("/directories/{directory_id}", response_model=DirectoryResponseDto)
async def edit_directory(directory_id: int, directory_update_dto: DirectoryUpdateDto, db: Session = Depends(get_db)):
    updated_directory = update_directory(directory_id, directory_update_dto, db)
    if not updated_directory:
        raise HTTPException(status_code=404, detail="Directory not found")
    return updated_directory

@router.get("/directories/parent/{parent_id}", response_model=List[DirectoryResponseDto])
async def list_directories_by_parent(parent_id: int, db: Session = Depends(get_db)):
    return get_directories_by_parent_id(parent_id, db)

@router.get("/directories/root", response_model=List[DirectoryResponseDto])
async def list_root_directories(db: Session = Depends(get_db)):
    return get_root_directories(db)