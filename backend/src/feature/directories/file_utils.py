import os
import hashlib
from datetime import datetime
from typing import Dict, Any
from .dto import FileMeta, DirectoryMeta

def __hybird_hashing(file_path: str) -> str:
    return

def get_file_metadata(file_path: str) -> FileMeta:
    stats = os.stat(file_path)
    file_hash = hashlib.md5(open(file_path,'rb').read()).hexdigest()
    
    return FileMeta(
        name=os.path.basename(file_path),
        path=file_path,
        size=stats.st_size,
        create_date=datetime.fromtimestamp(stats.st_birthtime),
        modified_date=datetime.fromtimestamp(stats.st_mtime),
        hash=file_hash
    ) 

def get_directory_metadata(dir_path: str) -> DirectoryMeta:
    stats = os.stat(dir_path)
    
    return DirectoryMeta(
        name=os.path.basename(dir_path),
        path=dir_path,
        create_date=datetime.fromtimestamp(stats.st_birthtime),
        modified_date=datetime.fromtimestamp(stats.st_mtime)
    )

def diff(path: str) -> float:
    return os.path.getmtime(path)

def get_size(path: str) -> int:
    return os.path.getsize(path)
