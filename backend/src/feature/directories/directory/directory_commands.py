from sqlalchemy.orm import Session
from feature.directories.dto.directory_dto import DirectoryCreateDto, DirectoryUpdateDto, DirectoryResponseDto
from model import Directory

def add_directory(directory_create_dto: DirectoryCreateDto, db: Session) -> DirectoryResponseDto:
    new_directory = Directory(name=directory_create_dto.name, parent_id=directory_create_dto.parent_id)
    db.add(new_directory)
    db.commit()
    db.refresh(new_directory)
    return DirectoryResponseDto.model_validate(new_directory)

def remove_directory(directory_id: int, db: Session) -> bool:
    directory = db.query(Directory).filter(Directory.id == directory_id).first()
    if directory:
        db.delete(directory)
        db.commit()
        return True
    return False

def update_directory(directory_id: int, directory_update_dto: DirectoryUpdateDto, db: Session) -> DirectoryResponseDto:
    directory = db.query(Directory).filter(Directory.id == directory_id).first()
    if directory:
        directory.name = directory_update_dto.name
        db.commit()
        db.refresh(directory)
        return DirectoryResponseDto.model_validate(directory)
    else:
        return None  # Or raise an exception