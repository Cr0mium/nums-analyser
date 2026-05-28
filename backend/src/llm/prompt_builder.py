# src/llm/promots_builder.py

from backend.src.llm.prompts import PLANNER_PROMPT


def build_planner_prompt(metrics, query):

    return f"""
    {PLANNER_PROMPT}

    User query:
    {query}

    Analytics metrics:
    {metrics}
    """
