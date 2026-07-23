from app.models.message import Message,Role
from app.models.chat_request import ChatRequest
from app.llm.factory import ProviderFactory

class ChatSession :
    def __init__(self, system_prompt: str | None = None):
        self.provider = ProviderFactory.create()
        self.history : list[Message] = []
        
        if system_prompt:
            self.history.append(
                Message(
                    role=Role.SYSTEM,
                    content=system_prompt
                )
            )
        
        
    
    def send(self, msg: str) -> str:
        self.history.append(Message(
            role=Role.USER,
            content= msg
        ))
        
        request = ChatRequest(
            messages=self.history
        )
        
        response = self.provider.chat(request)
        
        self.history.append(response.message)
        
        return response.message.content