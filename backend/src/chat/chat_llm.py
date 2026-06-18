# src/chat/chat_llm.py

import json

from backend.src.llm.openai_client import openai_client
from backend.src.llm.prompts import CHAT_PROMPT


class ChatLLM:
    def answer(
        self,
        session: dict,
        query: str,
    ) -> str:

        messages = [
            {
                "role": "system",
                "content": CHAT_PROMPT,
            },
            {
                "role": "system",
                "content": f"""
                Dataset schema:
                {json.dumps(session["schema"])}

                Dataset analytics:
                {json.dumps(session["analytics"])}
                """,
            },
        ]

        # Previous conversation
        messages.extend(session["chat_history"])

        # Current user message (MOST IMPORTANT)
        messages.append(
            {
                "role": "user",
                "content": query,
            }
        )

        print(messages)

        return openai_client.generate(messages=messages)
