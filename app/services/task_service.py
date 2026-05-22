from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskResponse


class TaskService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_task(self, payload: TaskCreate) -> TaskResponse:
        task = Task(
            title=payload.title,
            description=payload.description,
            priority=payload.priority.value,
            completed=False,
        )
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return TaskResponse.model_validate(task)

    def get_all_tasks(self) -> list[TaskResponse]:
        tasks = self.db.query(Task).all()
        return [TaskResponse.model_validate(t) for t in tasks]


def get_task_service(db: Session = Depends(get_db)) -> TaskService:
    return TaskService(db)
