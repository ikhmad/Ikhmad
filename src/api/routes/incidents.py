from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, status

from src.domain.incidents import CreateIncidentRequest, Incident, IncidentStatus
from src.services.incidents import (
    IncidentNotFoundError,
    create_incident,
    get_incident,
    list_incidents,
    update_incident_status,
)

router = APIRouter(prefix="/incidents", tags=["incidents"])


class UpdateIncidentStatusRequest(BaseModel):
    status: IncidentStatus


@router.post("", response_model=Incident, status_code=status.HTTP_202_ACCEPTED)
def submit_incident(request: CreateIncidentRequest) -> Incident:
    return create_incident(request)


@router.get("", response_model=list[Incident])
def get_incidents() -> list[Incident]:
    return list_incidents()


@router.get("/{incident_id}", response_model=Incident)
def get_incident_by_id(incident_id: str) -> Incident:
    try:
        return get_incident(incident_id)
    except IncidentNotFoundError:
        raise HTTPException(status_code=404, detail="Incident not found") from None


@router.patch("/{incident_id}/status", response_model=Incident)
def change_incident_status(
    incident_id: str,
    request: UpdateIncidentStatusRequest,
) -> Incident:
    """
    Public prototype status transition endpoint.

    Production authorization, validation policies and proprietary
    decision rules are intentionally out of scope.
    """
    try:
        return update_incident_status(incident_id, request.status)
    except IncidentNotFoundError:
        raise HTTPException(status_code=404, detail="Incident not found") from None
