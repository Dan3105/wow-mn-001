import uuid
from app.db import db
from .base import BaseModel

class Project(BaseModel):
    id: str = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    created_on = db.Column(db.DateTime, server_default=db.func.now())

    name: str = db.Column(db.String)
    description: str = db.Column(db.String)
    collection_name = db.Column(db.String)
    user_id: int = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", back_populates="projects")

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "user_id": self.user_id,
            "collection_name": self.collection_name,
        }