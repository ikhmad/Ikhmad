from datetime import datetime, timezone
from enum import StrEnum
from uuid import uuid4

from pydantic import BaseModel, Field

from src.domain.common import Location


class SOSStatus(StrEnum):
    RECEIVED = "RECEIVED"
    ACKNOWLEDGED = "ACKNOWLEDGED"
    RESOLVED = "RESOLVED"
    CANCELLED = "CANCELLED"


class Vulnerability(StrEnum):
    CHILDREN = "CHILDREN"
    ELDERLY = "ELDERLY"
    REDUCED_MOBILITY = "REDUCED_MOBILITY"
    INJURED = "INJURED"


class CreateSOSRequest(BaseModel):
    location: Location
    people_count: int = Field(default=1, ge=1, le=100)
    vulnerabilities: list[Vulnerability] = []
    situation: str | None = Field(default=None, max_length=300)
    incident_id: str | None = None


class SOSRequest(BaseModel):
    sos_id: str
    status: SOSStatus
    location: Location
    people_count: int
    vulnerabilities: list[Vulnerability]
    situation: str | None
    incident_id: str | None
    created_at: datetime
    updated_at: datetime


def new_sos(request: CreateSOSRequest) -> SOSRequest:
    now = datetime.now(timezone.utc)
    return SOSRequest(
        sos_id=f"SOS-{uuid4().hex[:10].upper()}",
        status=SOSStatus.RECEIVED,
        location=request.location,
        people_count=request.people_count,
        vulnerabilities=request.vulnerabilities,
        situation=request.situation,
        incident_id=request.incident_id,
        created_at=now,
        updated_at=now,
    )
