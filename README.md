# 🛡️ SOC Analyst AI Agent

An end-to-end AI-powered Security Operations Center (SOC) Analyst Assistant built using Machine Learning, FastAPI, Streamlit, and Docker.

The system simulates a real-world SOC workflow by performing:

* Threat Detection
* Incident Prioritization
* Automated Response Recommendation

The platform enables security analysts to analyze alerts, assess risks, prioritize incidents, and receive recommended remediation actions through an interactive dashboard.

---

# 🚀 Project Overview

SOC Analyst AI Agent is a production-style cybersecurity project designed to mimic real-world Security Operations Center workflows.

The solution processes security alerts from multiple enterprise sources and uses machine learning models to:

1. Detect whether an alert is malicious or benign.
2. Predict incident priority (P1–P4).
3. Recommend the most appropriate response action.

The project follows a complete MLOps-style pipeline including:

* Dataset Generation
* Data Preprocessing
* Model Training
* Model Serialization
* FastAPI Backend
* Streamlit Frontend
* Docker Containerization

---

# 🏗️ System Architecture

```text
┌─────────────────────┐
│ Streamlit Dashboard │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    FastAPI Backend  │
└──────────┬──────────┘
           │
 ┌─────────┼─────────┐
 ▼         ▼         ▼

Threat   Priority   Response
Model     Model      Model

 ▼         ▼         ▼

Threat  Incident   Recommended
Label   Priority     Action
```

---

# 📊 Dataset Information

Synthetic enterprise cybersecurity dataset containing:

* 200,000 records
* Authentication events
* Network telemetry
* Endpoint telemetry
* Threat intelligence indicators
* Asset criticality information
* User behavior analytics
* MITRE ATT&CK-inspired features
* Risk scoring attributes

---

## Features

### Authentication Features

* failed_login_count
* geo_anomaly

### Threat Intelligence Features

* known_ioc_match
* malware_detected

### Asset Features

* asset_criticality

### User Risk Features

* user_risk_score
* overall_risk_score

### Alert Metadata

* alert_source
* alert_type
* severity_raw

---

# 🎯 Machine Learning Tasks

## 1. Threat Detection Model

Predicts:

```text
Benign
Malicious
```

### Input Features

* Alert Source
* Alert Type
* Severity
* IOC Match
* Malware Indicators
* User Risk
* Asset Criticality

### Output

```text
Threat Label
```

---

## 2. Incident Priority Model

Predicts:

```text
P1
P2
P3
P4
```

### Output

```text
Incident Priority
```

---

## 3. Response Recommendation Model

Predicts:

```text
Contain Host
Block IP
Disable Account
Reset Credentials
Investigate Endpoint
Monitor Activity
Close Alert
```

### Output

```text
Recommended Response Action
```

---

# ⚙️ Technology Stack

## Programming Language

* Python 3.11

## Machine Learning

* Scikit-Learn
* Pandas
* NumPy
* Joblib

## Backend

* FastAPI
* Uvicorn
* Pydantic

## Frontend

* Streamlit

## Containerization

* Docker
* Docker Compose

---

# 📂 Project Structure

```text
soc-analyst-ml/
│
├── backend/
│   ├── api/
│   ├── services/
│   ├── schemas/
│   ├── models/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── pages/
│   ├── services/
│   ├── data/
│   ├── streamlit_app.py
│   └── requirements.txt
│
├── notebooks/
│   ├── threat_detection.ipynb
│   ├── incident_priority.ipynb
│   └── response_recommendation.ipynb
│
├── docker-compose.yml
├── README.md
└── docs/
```

---

# 🔌 API Endpoints

## Analyze Alert

```http
POST /analyze
```

### Example Request

```json
{
  "alert_data": {
    "alert_source": "SIEM",
    "alert_type": "Malware",
    "severity_raw": 10,
    "failed_login_count": 50,
    "geo_anomaly": 1,
    "known_ioc_match": 1,
    "malware_detected": 1,
    "asset_criticality": "Critical",
    "user_risk_score": 100,
    "overall_risk_score": 150
  }
}
```

### Example Response

```json
{
  "timestamp": "2026-06-16T18:21:32Z",
  "threat": "Malicious",
  "priority": "P1",
  "recommendation": "Contain Host",
  "confidence": {
    "threat": 1.0,
    "priority": 0.66,
    "recommendation": 0.42
  }
}
```

---

## Health Check

```http
GET /health
```

### Response

```json
{
  "status": "healthy",
  "models_loaded": true,
  "service": "SOC Analyst AI"
}
```

---

# 🖥️ Dashboard Features

## Alert Analyzer

* Security alert input form
* Real-time AI analysis
* Threat prediction
* Priority prediction
* Response recommendation
* Confidence visualization

## Incident History

* Incident logging
* KPI metrics
* Threat distribution
* Priority distribution
* CSV export

## System Health

* Backend monitoring
* Model status monitoring
* Service health checks

---

# 🐳 Docker Deployment

## Build Containers

```bash
docker compose build --no-cache
```

## Run Application

```bash
docker compose up
```

---

## Access Services

### Streamlit Dashboard

```text
http://localhost:8501
```

### FastAPI Swagger UI

```text
http://localhost:8000/docs
```

---

# 📸 Screenshots


```text
docs/screenshots/
```

Included screenshots:

* Alert Analyzer
* Incident History
* System Health
* Swagger API
* Docker Containers Running

---

# 🔮 Future Enhancements

* SIEM Integration (Splunk / QRadar)
* Real-Time Log Streaming
* LLM-Powered Incident Investigation
* Threat Hunting Assistant
* MITRE ATT&CK Mapping
* SOC Copilot using Generative AI
* Cloud Deployment (AWS / Azure)

---

