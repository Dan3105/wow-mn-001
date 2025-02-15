import uuid
from app.db import db
from .base import BaseModel
from .association import file_conversation

class Conversation(BaseModel):
    id: str = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    created_on = db.Column(db.DateTime, server_default=db.func.now())

    retriever: str = db.Column(db.String)
    memory: str = db.Column(db.String)
    llm: str = db.Column(db.String)

    file_id: int = db.Column(db.Integer, db.ForeignKey("file.id"), nullable=False)
    file = db.relationship("file", back_populates="conversations")

    user_id: int = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", back_populates="conversations")

    messages = db.relationship(
        "Message", back_populates="conversation", order_by="Message.created_on"
    )

    files = db.relationship(
        "Pdf",
        secondary=file_conversation,
        back_populates="conversations"
    )

    def as_dict(self):
        return {
            "id": self.id,
            "file_id": self.file_id,
            "messages": [m.as_dict() for m in self.messages],
            "files": [p.as_dict() for p in self.files],
        }
