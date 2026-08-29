# 🛡️ LangGraph Sequential Code Auditor & Modernization Pipeline

An autonomous, multi-agent developer tool powered by **LangGraph**, **Google Gemini (1.5 Flash)**, and **Streamlit**. The system ingests raw, un-optimized, or buggy Python code and executes a sequential 3-stage agent pipeline to audit security vulnerabilities, fix syntax/runtime bugs according to PEP8 standards, and generate a side-by-side comparison report with full download capabilities.

LIVE HERE: [click me](https://langgraph-code-auditor-qhhk7ztq5zaux3itagsfhm.streamlit.app/) 
---

## 🌟 Key Features

* **Automated Code Auditing**: Identifies syntax errors, runtime exceptions, resource leaks, and critical security vulnerabilities (e.g., SQL Injections, hardcoded secrets).
* **Bug Fix & PEP8 Refactoring**: Rewrites code into clean, secure, type-annotated, and runnable Python code.
* **Side-by-Side Comparison & Documentation**: Generates a matrix contrasting the original vs refactored implementations, docstring summaries, and deployment checklists.
* **Streamlit Live UI & State Persistence**: Real-time agent status tracking with session-persisted output tabs that stay intact after file downloads.
* **Download & One-Click Copy**: Direct downloads for the refactored code (`.py`) and the complete Markdown audit report (`.md`).

---

## 🏗️ Architecture & Sequential Workflow

The pipeline utilizes **LangGraph** to manage state transitions safely via Python `TypedDict` schemas:

```text
[Input Raw Code] 
       │
       ▼
┌──────────────┐
│ Scanner Agent│  --> Audits security vulnerabilities, syntax issues & runtime bugs
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Refactor Agent│ --> Generates production-ready, PEP8-compliant runnable code
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Docs Agent  │  --> Produces comparison matrix, docstrings & downloadable report
└──────┬───────┘
       │
       ▼
[Final Output Tabs & Download Actions]

```

---

## 📁 Project Structure

```text
langgraph-code-auditor/
│
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variables template
├── README.md                 # Project documentation
│
├── src/
│   ├── __init__.py
│   ├── state.py              # TypedDict state definition
│   ├── utils.py              # LLM initializers and text/code parsers
│   ├── graph.py              # LangGraph sequential workflow definition
│   │
│   └── agents/
│       ├── __init__.py
│       ├── scanner.py        # Error, bug & security scanning agent
│       ├── refactor.py       # Code refactoring & fixing agent
│       └── docs.py           # Documentation & comparison agent
│
└── app.py                    # Streamlit frontend application

```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone [https://github.com/your-username/langgraph-code-auditor.git](https://github.com/your-username/langgraph-code-auditor.git)
cd langgraph-code-auditor

```

### 2. Create and Activate a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

---

## 🔑 Providing Your Gemini API Key

You can provide your Google Gemini API key using either of the following methods:

### Option A: Via Streamlit UI Sidebar (Recommended)

You do **not** need to hardcode your API key or configure a `.env` file before running. Simply launch the application and enter your key in the input box located on the left sidebar:

1. Launch the app (`streamlit run app.py`).
2. Navigate to the left sidebar labeled **⚙️ Configuration**.
3. Paste your key in the **Gemini API Key** field.
4. Click **🚀 Run Multi-Agent Audit Pipeline**.

### Option B: Via `.env` File

Create a `.env` file in the root directory:

```bash
GOOGLE_API_KEY=your_actual_gemini_api_key_here

```

---

## 🚀 Running the Application

Start the Streamlit application with the following command:

```bash
streamlit run app.py

```

1. Open your browser at `http://localhost:8501`.
2. Enter your **Gemini API Key** in the sidebar.
3. Paste any broken or un-optimized Python snippet into the text area.
4. Click **Run Multi-Agent Audit Pipeline** to review the generated code and download the reports.

---

## 🛠️ Technology Stack

* **Language:** Python 3.10+
* **Orchestration:** LangGraph (StateGraph)
* **LLM Framework:** LangChain / `langchain-google-genai`
* **Model:** Google Gemini 1.5 Flash
* **Frontend:** Streamlit
* **State Management:** Python `TypedDict`

