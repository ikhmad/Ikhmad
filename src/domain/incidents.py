from datetime import datetime, timezone
from enum import StrEnum
from uuid import uuid4

from pydantic import BaseModel, Field

from src.domain.common import Location


class IncidentStatus(StrEnum):
    REPORTED = "REPORTED"
    UNDER_REVIEW = "UNDER_REVIEW"
    PROBABLE = "PROBABLE"
    CONFIRMED = "CONFIRMED"
    ACTIVE = "ACTIVE"
    CONTROLLED = "CONTROLLED"
    CLOSED = "CLOSED"
    REJECTED = "REJECTED"


class ObservationType(StrEnum):
    SMOKE = "SMOKE"
    FLAMES = "FLAMES"
    SMOKE_OR_FIRE = "SMOKE_OR_FIRE"
    OTHER = "OTHER"


class CreateIncidentRequest(BaseModel):
    location: Location
    observation_type: ObservationType
    note: str | None = Field(default=None, max_length=500)


class Incident(BaseModel):
    incident_id: str
    status: IncidentStatus
    location: Location
    observation_type: ObservationType
    note: str | None = None
    created_at: datetime
    updated_at: datetime


def new_incident(request: CreateIncidentRequest) -> Incident:
    now = datetime.now(timezone.utc)
    return Incident(
        incident_id=f"IKH-{uuid4().hex[:10].upper()}",
        status=IncidentStatus.REPORTED,
        location=request.location,
        observation_type=request.observation_type,
        note=request.note,
        created_at=now,
        updated_at=now,
    )
