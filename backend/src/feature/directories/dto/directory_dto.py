from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from src.feature.directories.dto.file_dto import FileResponseDto

class DirectoryCreateDto(BaseModel):
    name: str
    parent_id: Optional[int] = None

class DirectoryUpdateDto(BaseModel):
    name: str

class DirectoryResponseDto(BaseModel):
    id: int
    name: str
    parent_id: Optional[int]
    created_at: datetime
    updated_at: datetime

    subdirectories: Optional[list['DirectoryResponseDto']] = None
    subfiles: Optional[list['FileResponseDto']] = None
    
    class Config:
        from_attributes = True
