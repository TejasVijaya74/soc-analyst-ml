import pandas as pd
from datetime import datetime
from services.model_loader import (
    THREAT_MODEL,
    PRIORITY_MODEL,
    PRIORITY_ENCODER,
    RESPONSE_MODEL,
    RESPONSE_ENCODER
)


class SOCPredictor:

    @staticmethod
    def predict(payload):

        df = pd.DataFrame([payload])

        # -------------------------
        # Threat Detection
        # -------------------------

        threat_pred = THREAT_MODEL.predict(df)[0]

        threat_prob = float(
            max(
                THREAT_MODEL.predict_proba(df)[0]
            )
        )

        threat_label = (
            "Malicious"
            if threat_pred == 1
            else "Benign"
        )

        # Add prediction for Priority Model
        df["threat_label"] = threat_pred

        # -------------------------
        # Priority Prediction
        # -------------------------

        priority_pred = PRIORITY_MODEL.predict(df)

        priority_prob = float(
            max(
                PRIORITY_MODEL.predict_proba(df)[0]
            )
        )

        priority_label = (
            PRIORITY_ENCODER
            .inverse_transform(priority_pred)[0]
        )

        # Add prediction for Response Model
        df["priority_label"] = priority_pred[0]

        # -------------------------
        # Response Recommendation
        # -------------------------

        response_pred = RESPONSE_MODEL.predict(df)

        response_prob = float(
            max(
                RESPONSE_MODEL.predict_proba(df)[0]
            )
        )

        response_label = (
            RESPONSE_ENCODER
            .inverse_transform(response_pred)[0]
        )

        return {
            "timestamp": datetime.utcnow().isoformat(),
            "threat": threat_label,
            "priority": priority_label,
            "recommendation": response_label,
            "confidence": {
                "threat": round(threat_prob, 4),
                "priority": round(priority_prob, 4),
                "recommendation": round(response_prob, 4)
            }
        }