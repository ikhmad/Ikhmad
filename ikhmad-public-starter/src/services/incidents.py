from datetime import datetime, timezone

from src.domain.incidents import (
    CreateIncidentRequest,
    Incident,
    IncidentStatus,
    new_incident,
)
from src.repositories.memory import store


class IncidentNotFoundError(KeyError):
    pass


def create_incident(request: CreateIncidentRequest) -> Incident:
    incident = new_incident(request)
    store.incidents[incident.incident_id] = incident
    return incident


def list_incidents() -> list[Incident]:
    return sorted(
        store.incidents.values(),
        key=lambda item: item.created_at,
        reverse=True,
    )


def get_incident(incident_id: str) -> Incident:
    incident = store.incidents.get(incident_id)
    if incident is None:
        raise IncidentNotFoundError(incident_id)
    return incident


def update_incident_status(incident_id: str, status: IncidentStatus) -> Incident:
    incident = get_incident(incident_id)
    updated = incident.model_copy(
        update={
            "status": status,
            "updated_at": datetime.now(timezone.utc),
        }
    )
    store.incidents[incident_id] = updated
    return updated
