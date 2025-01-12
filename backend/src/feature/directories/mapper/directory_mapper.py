from model.directories import Directory
from directories.dto import DirectoryCreateDto, DirectoryResponseDto, DirectoryUpdateDto

class DirectoryMapper:
    @staticmethod
    def to_entity(dto: DirectoryCreateDto) -> Directory:
        return Directory(
            name=dto.name,
            parent_id=dto.parent_id
        )
    
    @staticmethod
    def to_dto(entity: Directory) -> DirectoryResponseDto:
        return DirectoryResponseDto.model_validate(entity)

    @staticmethod
    def update_entity(entity: Directory, dto: DirectoryUpdateDto) -> None:
        for field, value in dto.model_dump().items():
            setattr(entity, field, value)
