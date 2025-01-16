from fastapi import HTTPException
from typing import Dict, Any
import os
from ..file_utils import get_file_metadata, get_directory_metadata
from ..dto import DirectoryMeta, FileMeta, ResourceMeta

class DirectoryOperations:
    def __init__(self, path: str):
        home_path = os.getenv("OS_PATH")
        self.dir_path = os.path.join(home_path, path)

    def list_directory(self) -> ResourceMeta:
        curr_path = self.dir_path
        folders_data: list[DirectoryMeta] = [] 
        files_data: list[FileMeta] = []

        if os.path.exists(curr_path):
            for item in os.listdir(curr_path):
                full_path = os.path.join(curr_path, item)
                if os.path.isdir(full_path):
                    metadata = get_directory_metadata(full_path)
                    folders_data.append(metadata)
                else:
                    metadata = get_file_metadata(full_path)
                    files_data.append(metadata)
            
            prevPath = "." if os.path.join(curr_path, '..') == os.getenv("OS_PATH") else os.path.join(curr_path, '..')

            return ResourceMeta(
                parent_path=prevPath,
                path=curr_path,
                directories=folders_data,
                files=files_data
            )
        raise HTTPException(status_code=404, detail="Directory not found")

    def create_directory(self, folder: str, name: str) -> Dict[str, Any]:
        new_dir_path = os.path.join(self.home_path, folder, name)
        try:
            os.mkdir(new_dir_path)
            return get_directory_metadata(new_dir_path)
        except IOError as e:
            raise HTTPException(status_code=500, detail=str(e))
