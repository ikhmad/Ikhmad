from fastapi import APIRouter, HTTPException, status

from src.domain.sos import CreateSOSRequest, SOSRequest
from src.services.sos import SOSNotFoundError, create_sos, get_sos, list_sos

router = APIRouter(prefix="/sos", tags=["sos"])


@router.post("", response_model=SOSRequest, status_code=status.HTTP_202_ACCEPTED)
def submit_sos(request: CreateSOSRequest) -> SOSRequest:
    return create_sos(request)


@router.get("", response_model=list[SOSRequest])
def get_sos_requests() -> list[SOSRequest]:
    return list_sos()


@router.get("/{sos_id}", response_model=SOSRequest)
def get_sos_by_id(sos_id: str) -> SOSRequest:
    try:
        return get_sos(sos_id)
    except SOSNotFoundError:
        raise HTTPException(status_code=404, detail="SOS request not found") from None
