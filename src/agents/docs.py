from langchain_core.messages import HumanMessage
from src.state import CodeState
from src.utils import get_llm, extract_text

def docs_agent(state: CodeState) -> dict:
    llm = get_llm(temperature=0.2)
    original_code = state.get("raw_code", "")
    refactored_code = state.get("refactored_code", "")
    audit_report = state.get("audit_report", "")

    prompt = f"""
You are a Technical Lead and Systems Architect.
Generate a structured Code Comparison & Modernization Report comparing the Original Code against the Refactored Code.

Use the following Markdown format:
# 📋 Code Audit & Transformation Report

## 1. Summary of Changes
Detailed breakdown of what bugs were resolved and architecture improvements made.

## 2. Side-by-Side Comparison Matrix
| Aspect | Original Implementation | Refactored Implementation | Impact & Optimization |
|---|---|---|---|
| Syntax & Runtime Safety | ... | ... | ... |
| Security & Input Handling | ... | ... | ... |
| Resource Management | ... | ... | ... |
| Coding Standards (PEP8) | ... | ... | ... |

## 3. Function Signatures & Documentation
Usage instructions and docstring summary for the refactored code.

## 4. Production Readiness Checklist
- [x] Syntax & Bug Free
- [x] Secured Against Injections / Leaks
- [x] Type Hinting & PEP8 Verified

---
Original Code:
```python
{original_code}
Refactored Code:

Python
{refactored_code}
Audit Findings:
{audit_report}
"""
    response = llm.invoke([HumanMessage(content=prompt)])
    return {
    "comparison_report": extract_text(response.content),
    "current_step": "Documentation & Comparison Completed"
    }