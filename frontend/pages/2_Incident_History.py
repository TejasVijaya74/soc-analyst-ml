import streamlit as st
import pandas as pd

from services.history_service import (
    load_history
)

st.title("📜 Incident History")

history = load_history()

if history.empty:
    st.warning("No incidents recorded yet.")
    st.stop()

# KPI Cards

total_incidents = len(history)

malicious = len(
    history[
        history["threat"] == "Malicious"
    ]
)

p1_count = len(
    history[
        history["priority"] == "P1"
    ]
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Incidents",
    total_incidents
)

col2.metric(
    "Malicious Alerts",
    malicious
)

col3.metric(
    "P1 Incidents",
    p1_count
)

st.divider()

st.subheader("Incident Records")

st.dataframe(
    history,
    width="stretch"
)

st.divider()

st.subheader("Threat Distribution")

threat_counts = (
    history["threat"]
    .value_counts()
)

st.bar_chart(threat_counts)

st.divider()

st.subheader("Priority Distribution")

priority_counts = (
    history["priority"]
    .value_counts()
)

st.bar_chart(priority_counts)

st.divider()

csv = history.to_csv(index=False)

st.download_button(
    label="⬇ Download Incident Report",
    data=csv,
    file_name="incident_history.csv",
    mime="text/csv"
)