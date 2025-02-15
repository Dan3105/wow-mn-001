from app.db import db

# Association table for the many-to-many relationship between Pdf and Conversation
file_conversation = db.Table('file_conversation',
    db.Column('file_id', db.String, db.ForeignKey('file.id')),
    db.Column('conversation_id', db.String, db.ForeignKey('conversation.id'))
)
