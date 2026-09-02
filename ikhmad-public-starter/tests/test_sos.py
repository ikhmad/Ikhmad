from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_submit_sos():
    response = client.post(
        "/api/v1/sos",
        json={
            "location": {
                "latitude": 36.73,
                "longitude": 4.42,
                "accuracy_meters": 12
            },
            "people_count": 2,
            "vulnerabilities": ["ELDERLY"],
            "situation": "Road blocked - synthetic demo"
        },
    )

    assert response.status_code == 202
    data = response.json()
    assert data["status"] == "RECEIVED"
    assert data["people_count"] == 2
