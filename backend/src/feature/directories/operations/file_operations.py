from fastapi import HTTPException, UploadFile
from typing import Dict, Any
import os
import shutil


class FileOperations:
    def __init__(self, parent_path: str):
        self.parent_path = parent_path

    async def upload_file(self, file: UploadFile, folder: str) -> Dict[str, Any]:
        # target_path = os.path.join(self.home_path, folder, file.filename)
        # try:
        #     with open(target_path, "wb") as buffer:
        #         shutil.copyfileobj(file.file, buffer)
        #     return get_file_metadata(target_path)
        # except Exception as e:
        #     raise HTTPException(status_code=500, detail=str(e))
        pass

    def move_file(self, source: str, destination: str, item_name: str) -> Dict[str, Any]:
        # source_path = os.path.join(self.home_path, source, item_name)
        # dest_path = os.path.join(self.home_path, destination, item_name)
        # try:
        #     shutil.move(source_path, dest_path)
        #     return get_file_metadata(dest_path)
        # except Exception as e:
        #     raise HTTPException(status_code=500, detail=str(e))
        pass