import streamlit as st

st.set_page_config(
    page_title="SOC Analyst AI",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ SOC Analyst AI")

st.markdown(
    """
    AI-Powered Security Operations Center Assistant
    """
)

st.sidebar.title(
    "🛡️ SOC Analyst AI"
)

st.sidebar.success(
    "Security Operations Center"
)

st.sidebar.info(
    """
    Available Pages:

    • Alert Analyzer

    • Incident History

    • System Health
    """
)