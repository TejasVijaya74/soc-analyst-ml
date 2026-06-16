import streamlit as st

from services.api_client import (
    health_check
)

st.title("⚙️ System Health")

try:

    health = health_check()

    st.success(
        f"Backend Status: {health['status']}"
    )

    col1, col2 = st.columns(2)

    col1.metric(
        "Service",
        health["service"]
    )

    col2.metric(
        "Models Loaded",
        str(
            health["models_loaded"]
        )
    )

    st.json(health)

except Exception as e:

    st.error(
        f"Backend Offline: {e}"
    )