from fastapi import APIRouter, Depends, status

from app.schemas.task import TaskCreate, TaskResponse
from app.services.task_service import TaskService, get_task_service

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/", response_model=list[TaskResponse])
def list_tasks(service: TaskService = Depends(get_task_service)) -> list[TaskResponse]:
    return service.get_all_tasks()


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(
    payload: TaskCreate,
    service: TaskService = Depends(get_task_service),
) -> TaskResponse:
    return service.create_task(payload)
