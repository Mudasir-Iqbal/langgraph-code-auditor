from langgraph.graph import StateGraph, END
from src.state import CodeState
from src.agents.scanner import scanner_agent
from src.agents.refactor import refactor_agent
from src.agents.docs import docs_agent

def create_code_auditor_graph():
    builder = StateGraph(CodeState)

    # Register agent nodes
    builder.add_node("scanner", scanner_agent)
    builder.add_node("refactor", refactor_agent)
    builder.add_node("docs", docs_agent)

    # Define sequential execution flow
    builder.set_entry_point("scanner")
    builder.add_edge("scanner", "refactor")
    builder.add_edge("refactor", "docs")
    builder.add_edge("docs", END)

    return builder.compile()