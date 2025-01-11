from src.dbcontext import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class Directory(Base):
    __tablename__ = 'directories'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey('directories.id'))
    parent = relationship('Directory', remote_side=[id])
    children = relationship('Directory', remote_side=[parent_id])
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self, name, parent_id):
        self.name = name
        self.parent_id = parent_id

    def __repr__(self):
        return f'<Directory {self.name}>'