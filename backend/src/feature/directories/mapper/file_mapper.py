from model.directories import File
from schema.directories.file_dto import FileCreateDto, FileResponseDto, FileUpdateDto

class FileMapper:
    @staticmethod
    def to_entity(dto: FileCreateDto) -> File:
        return File(
            name=dto.name,
            path=dto.path,
            size=dto.size,
            directory_id=dto.directory_id
        )
    
    @staticmethod
    def to_dto(entity: File) -> FileResponseDto:
        return FileResponseDto.model_validate(entity)

    @staticmethod
    def update_entity(entity: File, dto: FileUpdateDto) -> None:
        for field, value in dto.model_dump().items():
            setattr(entity, field, value)
