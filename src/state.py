from typing import TypedDict

class CodeState(TypedDict):
    raw_code: str
    audit_report: str
    refactored_code: str
    comparison_report: str
    current_step: str