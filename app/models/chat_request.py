from pydantic import BaseModel
from app.models.message import Message

class ChatRequest(BaseModel):
    messages:list[Message]
    temperature: float = 0.7
    max_tokens: int = 1024