from langchain_core.messages import HumanMessage
from src.state import CodeState
from src.utils import get_llm, extract_text

def scanner_agent(state: CodeState) -> dict:
    llm = get_llm(temperature=0.1)
    code = state.get("raw_code", "")

    prompt = f"""
You are an expert Code Quality, Bug Detection, and Security Specialist.
Analyze the provided code thoroughly for:
1. Syntax errors, NameErrors, Indentation issues, and TypeErrors.
2. Runtime exceptions, unhandled errors, and connection/resource leaks.
3. Security vulnerabilities (e.g., SQL injections, unsafe string interpolations).
4. PEP8 styling deviations and anti-patterns.

Format your output strictly using structured Markdown:
### 📌 Executive Summary
Brief summary of code health and risk rating.

### 🚨 Detected Issues Table
| Issue Category | Severity (🔴 High / 🟡 Medium / 🟢 Low) | Location / Trace | Issue Description & Potential Impact |
|---|---|---|---|
| (e.g. Runtime Bug / Security) | ... | ... | ... |

### 🛠️ Required Fixes & Recommendations
Step-by-step actionable remediation steps.

Code:
```python
{code}
"""
    response = llm.invoke([HumanMessage(content=prompt)])
    return {
    "audit_report": extract_text(response.content),
    "current_step": "Scanning Completed"
    }