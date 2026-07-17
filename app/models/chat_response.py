from app.models.message import Message

class ChatResponse(BaseModel):
    message: Message