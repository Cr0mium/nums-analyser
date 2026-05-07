# src/llm/generator.py

import os
import json
from openai import OpenAI


SYSTEM_PROMPT = """
You are a senior data analyst.

You are given structured analytics output from a CSV analytics engine.

Your task:
- Explain important trends
- Explain correlations
- Explain anomalies
- Give concise actionable insights
- Keep explanations practical and readable
- Do NOT hallucinate missing information
- Do NOT repeat raw JSON
- Use bullet points
- Mention statistical relationships carefully:
  correlation does not imply causation

Return a concise markdown report with sections:
1. Summary
2. Key Correlations
3. Trends
4. Anomalies
5. Recommendations
"""


class OpenAIAnalyzer:
    def __init__(
        self,
        api_key: str,
        model: str = "gpt-4.1-mini"
    ):
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def analyze(self, analytics_result: dict) -> str:

        analytics_json = json.dumps(
            analytics_result,
            indent=2
        )

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0.3,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": f"""
                    Analyze this analytics JSON:

                    {analytics_json}
                    """
                }
            ]
        )

        return response.choices[0].message.content