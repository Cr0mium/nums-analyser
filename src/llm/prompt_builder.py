# src/llm/promots_builder.py

from src.llm.prompts import PLANNER_PROMPT

def build_planner_prompt(metrics):

    return f"""
    {PLANNER_PROMPT}

    Metrics:
    {metrics}
    """
