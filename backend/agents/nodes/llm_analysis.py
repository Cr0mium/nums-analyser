# agents/nodes/llm_analysis.py

import os

from backend.src.llm.llm_analyser import OpenAIAnalyzer


def llm_analysis_node(state):

    try:
        analyzer = OpenAIAnalyzer()

        analytics_payload = {"metrics": state["metrics"]}

        insights = analyzer.analyze(analytics_payload, state["plan"], state["mode"])

        state["insights"] = insights

        return state

    except Exception as e:
        state["error"] = str(e)
        print("[EXCEPTION]:", e)
        return state


# upate to
#     analytics_payload = {
#     "metrics": state["metrics"],
#     "mode": state["mode"],
#     "response": state["response"]
# }
