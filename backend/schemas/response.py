from pydantic import BaseModel


class PredictionResponse(BaseModel):

    threat: str
    priority: str
    recommendation: str
    confidence: dict