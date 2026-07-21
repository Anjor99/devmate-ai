from app.llm.factory import ProviderFactory
from app.models.chat_request import ChatRequest
from app.models.message import Message,Role
provider = ProviderFactory.create()

request = ChatRequest(
    messages=[
        Message(
            role=Role.USER,
            content="Hello!"
        )
    ]
)

response = provider.chat(request)

print(response)