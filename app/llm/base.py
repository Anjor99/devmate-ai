from abc import ABC, abstractmethod
from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse

class LLMProvider(ABC):
    
    @abstractmethod
    def chat(self, request: ChatRequest) -> ChatResponse:
        pass