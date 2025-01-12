from sqlalchemy.orm import Session
from typing import List
from feature.directories.dto.file_dto import FileResponseDto

from model import File 

def get_files_by_directory_id(directory_id: int, db: Session) -> List[FileResponseDto]:
    files = (db.query(File)
             .filter(File.directory_id == directory_id)
             .all())
    return [FileResponseDto.model_validate(file) for file in files]

def get_files_from_root(db: Session) -> List[FileResponseDto]:
    files = (db.query(File)
             .filter(File.directory_id == None)
             .all())
    return [FileResponseDto.model_validate(file) for file in files]

def get_file_by_name(db: Session, file_name: str, dir_id: int) -> FileResponseDto:
    file = (db.query(File)
            .filter(File.name == file_name and File.directory_id == dir_id)
            .first())
    return FileResponseDto.model_validate(file) if file else None