import os
import httpx
from dotenv import load_dotenv

from models.llm import BaseLLM

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv(
    "OPENROUTER_MODEL",
    "nvidia/nemotron-3-ultra-550b-a55b:free"
)

if API_KEY is None:
    raise RuntimeError("OPENROUTER_API_KEY not found in environment variables.")


class OpenRouter(BaseLLM):
    BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

    async def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.2,
    ) -> str:

        payload = {
            "model": MODEL,
            "temperature": temperature,
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
        }

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        }

        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(
                self.BASE_URL,
                headers=headers,
                json=payload,
            )

        response.raise_for_status()

        data = response.json()

        try:
            return data["choices"][0]["message"]["content"]

        except (KeyError, IndexError):
            raise RuntimeError(
                f"Unexpected OpenRouter response:\n{data}"
            )