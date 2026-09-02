from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_publish_and_list_alert():
    created = client.post(
        "/api/v1/alerts",
        json={
            "title": "Evacuation order",
            "message": "Synthetic demonstration alert.",
            "severity": "CRITICAL"
        },
    )

    assert created.status_code == 201

    listed = client.get("/api/v1/alerts")
    assert listed.status_code == 200
    assert len(listed.json()) == 1
