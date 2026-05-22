from enum import Enum

from pydantic import BaseModel, Field


class TaskPriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: str | None = Field(default=None, max_length=1000)
    priority: TaskPriority = TaskPriority.medium


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    priority: TaskPriority
    completed: bool

    model_config = {"from_attributes": True}  # allows constructing from SQLAlchemy ORM objects
