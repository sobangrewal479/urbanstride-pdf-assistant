import os
from dotenv import load_dotenv


load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini").strip()


def has_valid_openai_key() -> bool:
    """
    Check whether a real OpenAI API key appears to be present.
    """
    return bool(OPENAI_API_KEY and OPENAI_API_KEY != "your_openai_api_key_here")