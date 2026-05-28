# src/llm/openai_client.py

from openai import OpenAI


class OpenAIClient:

    def __init__(
        self,
        api_key: str,
        model: str = "gpt-4.1-mini"
    ):

        self.client = OpenAI(api_key=api_key)

        self.model = model

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.3
    ) -> str:

        response = self.client.chat.completions.create(

            model=self.model,

            temperature=temperature,

            messages=[

                {
                    "role": "system",
                    "content": system_prompt
                },

                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )

        return response.choices[0].message.content