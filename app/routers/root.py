from fastapi import APIRouter, Depends

from app.services.hello_service import get_hello_service, HelloService
from app.models.hello import HelloResponse

router = APIRouter()


@router.get("/", response_model=HelloResponse)
def read_root(service: HelloService = Depends(get_hello_service)) -> HelloResponse:
    return service.get_greeting()
