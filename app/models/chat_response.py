from app.models.message import Message
from pydantic import BaseModel

class ChatResponse(BaseModel):
    message: Message