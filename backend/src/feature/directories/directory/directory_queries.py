from sqlalchemy.orm import Session
from typing import List
from feature.directories.dto.directory_dto import DirectoryResponseDto
from model import Directory  # Assuming you have a Directory model defined in models.py

def get_directories_by_parent_id(parent_id: int, db: Session) -> List[DirectoryResponseDto]:
    directories = (db.query(Directory)
                   .filter(Directory.parent_id == parent_id)
                   .all())
    return [DirectoryResponseDto.model_validate(directory) for directory in directories]

def get_root_directories(db: Session) -> List[DirectoryResponseDto]:
    directories = (db.query(Directory)
                   .filter(Directory.parent_id == None)
                   .all())
    return [DirectoryResponseDto.model_validate(directory) for directory in directories]

def get_root_directory_by_name(db: Session, dir_name: str, parent_id: int) -> DirectoryResponseDto:
    directory = db.query(Directory).filter(Directory.name == dir_name and Directory.parent_id == parent_id).first()
    return DirectoryResponseDto.model_validate(directory) if directory else None