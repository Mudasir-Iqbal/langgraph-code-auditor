from langchain_core.messages import HumanMessage
from src.state import CodeState
from src.utils import get_llm, extract_clean_code

def refactor_agent(state: CodeState) -> dict:
    llm = get_llm(temperature=0.1)
    code = state.get("raw_code", "")
    audit = state.get("audit_report", "")

    prompt = f"""
You are a Principal Python Engineer.
Rewrite and refactor the following original code to fix ALL syntax errors, runtime bugs, security vulnerabilities, and bad practices detailed in the Audit Report.

Guidelines:
1. Ensure the code is 100% bug-free, safe, secure, and production-ready.
2. Follow strict PEP8 conventions, add explicit type hints, and include proper docstrings.
3. Handle resources and database connections safely using context managers (`with` statements).
4. Return ONLY the final clean python code enclosed inside a single ```python ``` block.

Audit Report:
{audit}

Original Code:
```python
{code}
"""
    response = llm.invoke([HumanMessage(content=prompt)])
    clean_code = extract_clean_code(response.content)
    return {
    "refactored_code": clean_code,
    "current_step": "Refactoring Completed"
    }