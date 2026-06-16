import requests

BASE_URL = "http://backend:8000"


def analyze_alert(payload):

    response = requests.post(
        f"{BASE_URL}/analyze",
        json={
            "alert_data": payload
        }
    )

    return response.json()


def health_check():

    response = requests.get(
        f"{BASE_URL}/health"
    )

    return response.json()