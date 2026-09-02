from src.domain.sos import CreateSOSRequest, SOSRequest, new_sos
from src.repositories.memory import store


class SOSNotFoundError(KeyError):
    pass


def create_sos(request: CreateSOSRequest) -> SOSRequest:
    sos = new_sos(request)
    store.sos_requests[sos.sos_id] = sos
    return sos


def list_sos() -> list[SOSRequest]:
    return sorted(
        store.sos_requests.values(),
        key=lambda item: item.created_at,
        reverse=True,
    )


def get_sos(sos_id: str) -> SOSRequest:
    sos = store.sos_requests.get(sos_id)
    if sos is None:
        raise SOSNotFoundError(sos_id)
    return sos
