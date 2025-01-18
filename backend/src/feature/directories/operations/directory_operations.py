from fastapi import HTTPException
from typing import Dict, Any
import os
from ..file_utils import get_file_metadata, get_directory_metadata
from ..dto import DirectoryMeta, FileMeta, ResourceMeta

class DirectoryOperations:
    def __init__(self, path: str):
        self.home_path = os.getenv("OS_PATH")
        if not self.home_path:
            raise ValueError("OS_PATH environment variable is not set")
        self.dir_path = os.path.normpath(os.path.join(self.home_path, path))

    def list_directory(self) -> ResourceMeta:
        """
        Lists contents of a directory including files and subdirectories
        """
        if not os.path.exists(self.dir_path):
            raise HTTPException(status_code=404, detail="Directory not found")

        folders_data: list[DirectoryMeta] = []
        files_data: list[FileMeta] = []

        for item in os.listdir(self.dir_path):
            full_path = os.path.join(self.dir_path, item)
            if os.path.isdir(full_path):
                folders_data.append(get_directory_metadata(full_path))
            else:
                files_data.append(get_file_metadata(full_path))

        parent_path = os.path.dirname(self.dir_path)
        prev_path = self._get_previous_path(parent_path)

        return ResourceMeta(
            parent_path=prev_path,
            path=self.dir_path,
            directories=folders_data,
            files=files_data
        )

    def _get_previous_path(self, parent_path: str) -> str:
        """
        Determines the previous path based on home path constraints
        """
        os_path = os.path.normpath(self.home_path)
        parent_path = os.path.normpath(parent_path)
        
        if self.dir_path in (os_path, parent_path):
            return ""
        return parent_path

    def create_directory(self, folder: str, name: str) -> Dict[str, Any]:
        """
        Creates a new directory and returns its metadata
        """
        new_dir_path = os.path.join(self.home_path, folder, name)
        try:
            os.mkdir(new_dir_path)
            return get_directory_metadata(new_dir_path)
        except IOError as e:
            raise HTTPException(status_code=500, detail=str(e))
