from typing import Optional
from openai import OpenAI
from ..config import settings

_client: Optional[OpenAI] = None

def get_openai_client() -> Optional[OpenAI]:
    global _client
    if settings.OPENAI_API_KEY and _client is None:
        _client = OpenAI(api_key=settings.OPENAI_API_KEY)
    return _client
