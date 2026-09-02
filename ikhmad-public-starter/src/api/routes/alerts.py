from fastapi import APIRouter, status

from src.domain.alerts import Alert, CreateAlertRequest
from src.services.alerts import create_alert, list_alerts

router = APIRouter(prefix="/alerts", tags=["alerts"])


@router.post("", response_model=Alert, status_code=status.HTTP_201_CREATED)
def publish_alert(request: CreateAlertRequest) -> Alert:
    """
    Prototype endpoint.

    Production versions must require authorized operator roles.
    """
    return create_alert(request)


@router.get("", response_model=list[Alert])
def get_alerts() -> list[Alert]:
    return list_alerts()
