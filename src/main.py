from fastapi import FastAPI

from src.api.routes.alerts import router as alerts_router
from src.api.routes.health import router as health_router
from src.api.routes.incidents import router as incidents_router
from src.api.routes.sos import router as sos_router

app = FastAPI(
    title="IKHMAD Public API Prototype",
    version="0.1.0",
    description=(
        "Public-safe prototype API for IKHMAD. "
        "This service demonstrates incident, alert and SOS workflows. "
        "Proprietary decision-engine logic is intentionally excluded."
    ),
)

app.include_router(health_router)
app.include_router(incidents_router, prefix="/api/v1")
app.include_router(alerts_router, prefix="/api/v1")
app.include_router(sos_router, prefix="/api/v1")
