# agents/nodes/planner_agent.py

from src.llm.ollama_client import OllamaModel
from src.llm.prompt_builder import build_planner_prompt


ollama = OllamaModel()


def planner_agent_node(state):

    try:

        metrics = state["metrics"]

        correlations = metrics.get(
            "correlations",
            []
        )

        anomalies = metrics.get(
            "anomalies",
            []
        )

        # Sort strongest correlations first
        top_correlations = sorted(

            correlations,

            key=lambda x: abs(x["value"]),

            reverse=True

        )[:3]

        # Sort biggest anomalies first
        top_anomalies = sorted(

            anomalies,

            key=lambda x: abs(x["z_score"]),

            reverse=True

        )[:3]

        # Keep only strongest engine insights
        top_insights = metrics.get(
            "insights",
            []
        )[:5]

        # Compact planner payload
        planner_metrics = {

            "top_correlations": top_correlations,

            "top_anomalies": top_anomalies,

            "insights": top_insights
        }

        prompt = build_planner_prompt(
            planner_metrics
        )


        response = ollama.generate(

            prompt=prompt,

            max_new_tokens=512
        )

        print("[ollama_response]:")
        print(response)

        # Parse bullet-style output
        plan = [

        line.replace("*", "").replace("-", "").strip()

        for line in response.split("\n")

        if line.strip()

        ]
        print(plan)
        # Fallback
        if not plan:

            plan = [response.strip()]

        state["plan"] = plan

        return state

    except Exception as e:

        state["error"] = str(e)

        print("[planner_error]:", e)

        return state