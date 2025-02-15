import uuid
from app.db import db
from .base import BaseModel


class File(BaseModel):
    id: str = db.Column(
        db.String(), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    name: str = db.Column(db.String(80), nullable=False)
    user_id: int = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", back_populates="files")

    conversations = db.relationship(
        "Conversation",
        back_populates="file",
        order_by="desc(Conversation.created_on)",
    )

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
        }
