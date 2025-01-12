from sqlalchemy.orm import Session
from feature.directories.dto.file_dto import FileCreateDto, FileUpdateDto, FileResponseDto
from model import File

def add_file(file_create_dto: FileCreateDto, db: Session) -> FileResponseDto:
    new_file = File(
        name=file_create_dto.name,
        path=file_create_dto.path,
        size=file_create_dto.size,
        directory_id=file_create_dto.directory_id
    )
    db.add(new_file)
    db.commit()
    db.refresh(new_file)
    return FileResponseDto.model_validate(new_file)

def remove_file(file_id: int, db: Session) -> bool:
    file = db.query(File).filter(File.id == file_id).first()
    if file:
        db.delete(file)
        db.commit()
        return True
    return False

def update_file(file_id: int, file_update_dto: FileUpdateDto, db: Session) -> FileResponseDto:
    file = db.query(File).filter(File.id == file_id).first()
    if file:
        file.name = file_update_dto.name
        file.path = file_update_dto.path
        db.commit()
        db.refresh(file)
        return FileResponseDto.model_validate(file)
    else:
        return None  # Or raise an exception