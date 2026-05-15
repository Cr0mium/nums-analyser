# src/llm/llm_analyser.py

import json

from src.llm.prompts import SYSTEM_PROMPT
from src.llm.openai_client import OpenAIClient


class OpenAIAnalyzer:

    def __init__(
        self,
        api_key: str,
        model: str = "gpt-4.1-mini"
    ):

        self.client = OpenAIClient(
            api_key=api_key,
            model=model
        )

    def analyze(
        self,
        analytics_result: dict,
        plan: list[str],
        mode: str
    ) -> str:

        analytics_json = json.dumps(
            analytics_result,
            indent=2
        )

        planner_context = "\n".join(
            f"- {item}" for item in plan
        )

        user_prompt = f"""
        Dataset mode:
        {mode}

        Planner priorities:
        {planner_context}

        Analyze this analytics JSON:

        {analytics_json}
        """
        
        return self.client.generate(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=user_prompt
        )