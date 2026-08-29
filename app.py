import os
import streamlit as st
from dotenv import load_dotenv
from src.graph import create_code_auditor_graph

load_dotenv()

st.set_page_config(page_title="AI Code Auditor & Refactor", page_icon="🛡️", layout="wide")

st.title("🛡️ LangGraph Sequential Code Auditor & Fixer")
st.markdown("Automated Multi-Agent Pipeline: **Audit & Bug Scan ➔ Clean Refactor ➔ Comparison & Documentation**[cite: 1]")
# Sidebar Configuration
st.sidebar.header("⚙️ Configuration")
api_key_input = st.sidebar.text_input("Gemini API Key", type="password", value=os.getenv("GOOGLE_API_KEY", ""))
st.sidebar.markdown("🔗 [Get your Gemini API Key here](https://ai.google.dev/gemini-api/docs/api-key?utm_source=PMAX&utm_medium=display&utm_campaign=Cloud-SS-DR-AIS-FY26-global-pmax-1713578&utm_content=pmax&gad_source=1&gad_campaignid=23417432327&gbraid=0AAAAACn9t64YCK3TWTQZi_0VXxJXHmNe4&gclid=Cj0KCQjwhsrUBhDxARIsAN3AQSdNWiOxmuemSkI-bgwo2qk5alFWHrvsVDC1htPZtb2p6UYTCRUMjOkaArJkEALw_wcB)")
if api_key_input:
    os.environ["GOOGLE_API_KEY"] = api_key_input

# 1. Initialize Session State taake download ke waqt output delete na ho
if "audit_completed" not in st.session_state:
    st.session_state.audit_completed = False
if "final_state" not in st.session_state:
    st.session_state.final_state = {}

sample_bad_code = """def fetch_user_orders(user_id)
    import sqlite3
    db = sqlite3.connect("store.db")
    cur = db.cursor()
    
    # Bug 1: Missing colon in def line
    # Bug 2: SQL Injection Vulnerability
    cur.execute("SELECT * FROM orders WHERE user_id = " + str(user_id))
    results = cur.fetchall()
    
    # Bug 3: TypeError - accessing sqlite tuple via string key
    total_amount = 0
    for row in results:
        total_amount += row["price"]
        
    return results, total_amount
"""

raw_code = st.text_area("Input Code (Paste code with bugs, errors, or vulnerabilities):", value=sample_bad_code, height=220)

# Run Pipeline
if st.button("🚀 Run Multi-Agent Audit Pipeline", use_container_width=True):
    if not os.getenv("GOOGLE_API_KEY"):
        st.error("⚠️ Google Gemini API Key enter karein!")
    else:
        graph = create_code_auditor_graph()
        initial_state = {
            "raw_code": raw_code,
            "audit_report": "",
            "refactored_code": "",
            "comparison_report": "",
            "current_step": "Started"
        }

        status_box = st.empty()
        
        with st.spinner("Pipeline active: AI Agents analyzing and refactoring code..."):
            pipeline_state = {}
            for step in graph.stream(initial_state):
                for node_name, state_update in step.items():
                    if node_name == "scanner":
                        status_box.info("🔍 Scanner Agent: Code errors aur security flaws audit ho chuke hain...")
                    elif node_name == "refactor":
                        status_box.info("🛠️ Refactor Agent: Code fix aur PEP8 clean ho chuka hai...")
                    elif node_name == "docs":
                        status_box.success("✅ Docs Agent: Comparison matrix aur complete report tayar hai!")
                    pipeline_state.update(state_update)
            
            # Results ko Session State mein permanently save kar lein
            st.session_state.final_state = pipeline_state
            st.session_state.audit_completed = True

# 2. Render Results from Session State (Download click hone par bhi visible rahay ga)
if st.session_state.audit_completed and st.session_state.final_state:
    st.divider()
    final_state = st.session_state.final_state

    # Display Tabbed Results
    tab1, tab2, tab3 = st.tabs(["✨ Fixed & Clean Code", "🔍 Discovered Issues & Audit", "📑 Comparison Report & Download"])

    with tab1:
        st.subheader("Production-Ready Refactored Code")
        clean_code_out = final_state.get("refactored_code", "")
        st.code(clean_code_out, language="python")
        
        # Download Button without page reset
        st.download_button(
            label="📥 Download Fixed Code (.py)",
            data=clean_code_out,
            file_name="refactored_code.py",
            mime="text/x-python",
            key="download_code_btn"
        )

    with tab2:
        st.subheader("Comprehensive Code Audit")
        st.markdown(final_state.get("audit_report", "No report generated."))

    with tab3:
        st.subheader("Original vs Refactored Comparison Matrix")
        comparison_md = final_state.get("comparison_report", "No comparison report generated.")
        st.markdown(comparison_md)
        
        # Download Report Button without page reset
        st.download_button(
            label="📥 Download Full Audit & Comparison Report (.md)",
            data=comparison_md,
            file_name="code_audit_and_comparison_report.md",
            mime="text/markdown",
            key="download_report_btn"
        )