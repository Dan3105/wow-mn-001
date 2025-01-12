from backend.src.dbcontext.postgres import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

class Directory(Base):
    __tablename__ = 'directories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    parent_id = Column(Integer, ForeignKey('directories.id'), nullable=True)
    parent = relationship('Directory', remote_side=[id], back_populates='children')
    children = relationship('Directory', back_populates='parent', cascade='all, delete-orphan')
    files = relationship('File', back_populates='directory', cascade='all, delete-orphan')
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    __table_args__ = (UniqueConstraint('name', 'parent_id', name='_name_parent_uc'),)

    def __init__(self, name, parent_id=None):
        self.name = name
        self.parent_id = parent_id

    def __repr__(self):
        return f'<Directory {self.name}>'