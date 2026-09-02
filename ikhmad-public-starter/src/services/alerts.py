from src.domain.alerts import Alert, CreateAlertRequest, new_alert
from src.repositories.memory import store


def create_alert(request: CreateAlertRequest) -> Alert:
    alert = new_alert(request)
    store.alerts[alert.alert_id] = alert
    return alert


def list_alerts() -> list[Alert]:
    return sorted(
        store.alerts.values(),
        key=lambda item: item.created_at,
        reverse=True,
    )
