import streamlit as st

from services.api_client import analyze_alert
from datetime import datetime

from services.history_service import (
    save_incident
)
st.title("Alert Analyzer")

# Alert Inputs
alert_source = st.selectbox(
    "Alert Source",
    ["SIEM", "EDR", "Firewall"]
)

alert_type = st.selectbox(
    "Alert Type",
    ["Malware", "Phishing", "Brute Force"]
)

severity_raw = st.slider(
    "Severity",
    min_value=1,
    max_value=10,
    value=5
)

failed_login_count = st.number_input(
    "Failed Login Count",
    min_value=0,
    max_value=100,
    value=0
)

geo_anomaly = st.selectbox(
    "Geo Anomaly",
    [0, 1]
)

known_ioc_match = st.selectbox(
    "Known IOC Match",
    [0, 1]
)

malware_detected = st.selectbox(
    "Malware Detected",
    [0, 1]
)

asset_criticality = st.selectbox(
    "Asset Criticality",
    ["Low", "Medium", "High", "Critical"]
)

user_risk_score = st.slider(
    "User Risk Score",
    min_value=0,
    max_value=100,
    value=50
)

overall_risk_score = st.slider(
    "Overall Risk Score",
    min_value=0,
    max_value=200,
    value=50
)

# Analyze Button
if st.button("Analyze Alert"):

    payload = {
        "alert_source": alert_source,
        "alert_type": alert_type,
        "severity_raw": severity_raw,
        "failed_login_count": failed_login_count,
        "geo_anomaly": geo_anomaly,
        "known_ioc_match": known_ioc_match,
        "malware_detected": malware_detected,
        "asset_criticality": asset_criticality,
        "user_risk_score": user_risk_score,
        "overall_risk_score": overall_risk_score,
    }

    result = analyze_alert(payload)

    history_record = {
    "timestamp": datetime.now(),
    "threat": result["threat"],
    "priority": result["priority"],
    "recommendation": result["recommendation"]
}

    save_incident(history_record)

    st.success("Analysis Complete")

    if result["priority"] == "P1":
        st.error("🚨 Critical Incident Detected")

    elif result["priority"] == "P2":
        st.warning("⚠️ High Priority Incident")

    elif result["priority"] == "P3":
        st.info("ℹ️ Medium Priority Incident")

    else:
        st.success("✅ Low Priority Incident")

    # Metrics
    col1, col2, col3 = st.columns(3)

    col1.metric(
        label="Threat",
        value=result["threat"]
    )

    col2.metric(
        label="Priority",
        value=result["priority"]
    )

    col3.metric(
        label="Recommendation",
        value=result["recommendation"]
    )

    # Confidence Scores
    st.subheader("Confidence Scores")

    threat_confidence = result["confidence"]["threat"]

    st.progress(threat_confidence)

    st.write(
        f"Threat Confidence: {threat_confidence:.2%}"
    )

    # Optional: Display full response
    with st.expander("Raw Response"):
        st.json(result)