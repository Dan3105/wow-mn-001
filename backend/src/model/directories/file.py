from dbcontext.postgres import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

class File(Base):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    path = Column(String, nullable=False)
    size = Column(Integer)
    directory_id = Column(Integer, ForeignKey('directories.id'), nullable=False)
    directory = relationship('Directory', back_populates='files')
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    __table_args__ = (UniqueConstraint('name', 'directory_id', name='_name_directory_uc'),)

    def __init__(self, name, path, size, directory_id):
        self.name = name
        self.path = path
        self.size = size
        self.directory_id = directory_id

    def __repr__(self):
        return f'<File {self.name}>'