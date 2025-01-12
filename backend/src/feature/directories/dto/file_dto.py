from pydantic import BaseModel
from datetime import datetime

class FileCreateDto(BaseModel):
    name: str
    path: str
    size: int
    directory_id: int

class FileUpdateDto(BaseModel):
    id: int
    name: str
    path: str

class FileResponseDto(BaseModel):
    id: int
    name: str
    path: str
    size: int
    directory_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
