from pydantic.v1 import BaseModel, Extra

class Metadata(BaseModel, extra=Extra.allow):
    conversation_id: str
    user_id: str
    file_id: str


class ChatArgs(BaseModel, extra=Extra.allow):
    conversation_id: str
    file_id: str
    metadata: Metadata
    streaming: bool
