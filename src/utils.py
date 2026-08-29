import os
import re
from langchain_google_genai import ChatGoogleGenerativeAI

def get_llm(temperature: float = 0.1):
    """Google Gemini LLM ko safely environment variable ya parameter se initialize karta hai."""
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Google Gemini API Key missing hai! Streamlit sidebar ya .env file check karein.")
    
    return ChatGoogleGenerativeAI(
        model="gemini-3.5-flash",
        temperature=temperature,
        api_key=api_key
    )

def extract_text(response_content) -> str:
    """LangChain metadata/blocks response ko clean string mein convert karta hai."""
    if isinstance(response_content, str):
        return response_content.strip()
    elif isinstance(response_content, list):
        text_parts = [
            item.get("text", "") if isinstance(item, dict) else str(item)
            for item in response_content
        ]
        return "\n".join(text_parts).strip()
    return str(response_content).strip()

def extract_clean_code(text: str) -> str:
    """Markdown code blocks se sirf pure python code nikalta hai."""
    clean_text = extract_text(text)
    pattern = r"```(?:python)?\s*(.*?)\s*```"
    match = re.search(pattern, clean_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return clean_text.strip()