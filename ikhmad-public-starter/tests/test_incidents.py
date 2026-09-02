from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_submit_and_confirm_incident():
    create = client.post(
        "/api/v1/incidents",
        json={
            "location": {
                "latitude": 36.7538,
                "longitude": 3.0588,
                "accuracy_meters": 12
            },
            "observation_type": "SMOKE_OR_FIRE",
            "note": "Synthetic demonstration report"
        },
    )

    assert create.status_code == 202
    incident = create.json()
    assert incident["status"] == "REPORTED"

    update = client.patch(
        f"/api/v1/incidents/{incident['incident_id']}/status",
        json={"status": "CONFIRMED"},
    )

    assert update.status_code == 200
    assert update.json()["status"] == "CONFIRMED"


def test_list_incidents():
    client.post(
        "/api/v1/incidents",
        json={
            "location": {"latitude": 36.75, "longitude": 3.05},
            "observation_type": "SMOKE"
        },
    )
    response = client.get("/api/v1/incidents")
    assert response.status_code == 200
    assert len(response.json()) == 1
