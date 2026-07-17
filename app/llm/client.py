from groq import Groq
from app.config.settings import settings

client = Groq(api_key = settings.groq_api_key)


def chat(user_message: str) -> str:
    response = client.chat.completions.create(
        model=settings.model_name,
        messages=[
            {
                "role": "user",
                "content": user_message,
            }
        ],
    )

    return response.choices[0].message.content