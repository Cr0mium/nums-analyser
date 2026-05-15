from typing import TypedDict, Optional

class GraphState(TypedDict):
    df_json: str           # dataframe as json string
    schema: dict           # schema dict
    mode: str              # "personal" or "general"
    metrics: dict          # computed metrics
    insights: str          # final LLM insights
    error: Optional[str]   # error handling
    response: str
    plan: list[str]