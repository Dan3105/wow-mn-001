from pydantic import BaseModel
from datetime import datetime
from typing import List

class FileMeta(BaseModel):
    name: str
    path: str
    hash: str
    size: int
    create_date: datetime
    modified_date: datetime

class DirectoryMeta(BaseModel):
    name: str
    path: str
    create_date: datetime
    modified_date: datetime

class ResourceMeta(BaseModel):
    parent_path: str
    path: str
    directories: List[DirectoryMeta]
    files: List[FileMeta]
    