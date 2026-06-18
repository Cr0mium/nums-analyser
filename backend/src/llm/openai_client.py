# src/llm/openai_client.py


import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class OpenAIClient:
    def __init__(self, api_key: str, model: str = "gpt-4.1-mini"):

        self.client = OpenAI(api_key=api_key)

        self.model = model

    def generate(self, messages: list[dict], temperature: float = 0.3) -> str:

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=temperature,
            messages=messages,
        )

        return response.choices[0].message.content


openai_client = OpenAIClient(api_key=os.getenv("OPENAI_API_KEY"))
