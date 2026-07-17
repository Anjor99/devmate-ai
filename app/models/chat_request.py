from pydantic import BaseModel
from app.models.message import Message
from app.config.settings import settings

class ChatRequest(BaseModel):
    messages:list[Message]
    model: str = settings.model_name
    temperature: float = 0.7
    max_tokens: int = 1024