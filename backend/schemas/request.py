from pydantic import BaseModel


class AlertRequest(BaseModel):

    alert_data: dict