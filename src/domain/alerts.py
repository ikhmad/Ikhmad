from datetime import datetime, timezone
from enum import StrEnum
from uuid import uuid4

from pydantic import BaseModel, Field


class AlertSeverity(StrEnum):
    INFO = "INFO"
    MODERATE = "MODERATE"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class CreateAlertRequest(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    message: str = Field(min_length=1, max_length=600)
    severity: AlertSeverity
    incident_id: str | None = None


class Alert(BaseModel):
    alert_id: str
    title: str
    message: str
    severity: AlertSeverity
    incident_id: str | None
    created_at: datetime


def new_alert(request: CreateAlertRequest) -> Alert:
    return Alert(
        alert_id=f"ALT-{uuid4().hex[:10].upper()}",
        title=request.title,
        message=request.message,
        severity=request.severity,
        incident_id=request.incident_id,
        created_at=datetime.now(timezone.utc),
    )
