from fastapi import APIRouter

from schemas.request import AlertRequest

from services.predictor import (
    SOCPredictor
)

router = APIRouter()


@router.post("/analyze")
def analyze_alert(
    request: AlertRequest
):

    result = SOCPredictor.predict(
        request.alert_data
    )

    return result

@router.get("/health")
def health():

    return {
        "status": "healthy",
        "models_loaded": True,
        "service": "SOC Analyst AI"
    }