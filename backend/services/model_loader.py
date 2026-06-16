import joblib

THREAT_MODEL = joblib.load(
    "models/threat_detection_model.pkl"
)

PRIORITY_MODEL = joblib.load(
    "models/priority_model.pkl"
)

PRIORITY_ENCODER = joblib.load(
    "models/priority_encoder.pkl"
)

RESPONSE_MODEL = joblib.load(
    "models/response_model.pkl"
)

RESPONSE_ENCODER = joblib.load(
    "models/response_encoder.pkl"
)