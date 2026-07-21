from app.llm.base import LLMProvider
from app.llm.groq_provider import GroqProvider
from app.config.settings import settings

providers = {
    "groq": GroqProvider,
}


class ProviderFactory:
    @staticmethod
    def create() -> LLMProvider:
        if settings.provider in providers:
            return providers[settings.provider]()

        raise ValueError(
            f"Unsupported provider '{settings.provider}'. "
            "Supported providers: ['groq']"
        )