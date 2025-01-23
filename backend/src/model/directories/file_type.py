from dbcontext.postgres import Base
from sqlalchemy import Column, Integer, String, UniqueConstraint

class FileType(Base):
    __tablename__ = 'file_type'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    icon = Column(String, nullable=False)

    __table_args__ = (UniqueConstraint('name'))

    def __init__(self, name, path, size):
        self.name = name
        self.path = path
        self.size = size

    def __repr__(self):
        return f'<File {self.name}>'