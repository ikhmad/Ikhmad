from src.domain.alerts import Alert
from src.domain.incidents import Incident
from src.domain.sos import SOSRequest


class MemoryStore:
    """
    Development-only in-memory store.

    This is intentionally simple and is not suitable for production.
    A persistent database layer will replace it in the connected MVP.
    """

    def __init__(self) -> None:
        self.incidents: dict[str, Incident] = {}
        self.alerts: dict[str, Alert] = {}
        self.sos_requests: dict[str, SOSRequest] = {}

    def reset(self) -> None:
        self.incidents.clear()
        self.alerts.clear()
        self.sos_requests.clear()


store = MemoryStore()
