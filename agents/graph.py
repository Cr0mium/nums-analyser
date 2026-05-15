from langgraph.graph import StateGraph, END

from agents.state import GraphState
from agents.router import mode_router

from agents.nodes.personal_mode import personal_mode_node
from agents.nodes.general_mode import general_mode_node
from agents.nodes.llm_analysis import llm_analysis_node
from agents.nodes.planner_agent import planner_agent_node

builder = StateGraph(GraphState)

builder.add_node(
    "personal",
    personal_mode_node
)

builder.add_node(
    "general",
    general_mode_node
)

builder.add_node(
    "llm_analysis",
    llm_analysis_node
)

builder.add_node(
    "planner",
    planner_agent_node
)

builder.set_conditional_entry_point(
    mode_router,
    {
        "personal": "personal",
        "general": "general"
    }
)

builder.add_edge(
    "personal",
    "planner"
)

builder.add_edge(
    "general",
    "planner"
)

builder.add_edge(
    "planner",
    "llm_analysis"
)

builder.add_edge(
    "llm_analysis",
    END
)

graph = builder.compile()