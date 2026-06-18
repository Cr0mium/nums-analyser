# src/llm/llm_analyser.py

import json

from backend.src.llm.openai_client import openai_client
from backend.src.llm.prompts import SYSTEM_PROMPT


class OpenAIAnalyzer:
    def __init__(self):
        self.client = openai_client

    def analyze(
        self,
        analytics_result: dict,
        plan: list[str],
        mode: str,
    ) -> str:

        analytics_json = json.dumps(analytics_result, indent=2)

        planner_context = "\n".join(f"- {item}" for item in plan)

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": f"""
                Dataset mode:
                {mode}

                Planner priorities:
                {planner_context}

                Analytics JSON:
                {analytics_json}
                """,
            },
        ]

        return self.client.generate(messages)
