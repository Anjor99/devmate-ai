from app.llm.base import LLMProvider
from groq import Groq
from app.config.settings import settings
from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse
from app.models.message import Message, Role

class GroqProvider(LLMProvider):

    def __init__(self):
        self.client = Groq(api_key=settings.groq_api_key)

    def chat(self, request: ChatRequest) -> ChatResponse:
        """
        Send a chat request to Groq and return a provider-independent ChatResponse.
        """
        response = self.client.chat.completions.create(
            model=request.model,
            messages=self._to_groq_messages(request.messages),
            max_completion_tokens = request.max_tokens,
            temperature = request.temperature
        )

        return ChatResponse(
            message= Message(
                role=Role.ASSISTANT,
                content=self._from_groq_response(response)
            )
        )

    def _to_groq_messages(self, messages : list[Message]) -> list[dict[str,str]]:
        """
        Convert DevMate Message objects into the dictionary format
        required by the Groq API.
        """
        msg_list = []
        for msg in messages :
            msg_list.append({
                "role" : msg.role.value,
                "content" : msg.content
            })
        return msg_list

    def _from_groq_response(self, asst_response) -> str:
        """
        Extract the assistant's reply from the Groq response object.
        """
        return asst_response.choices[0].message.content