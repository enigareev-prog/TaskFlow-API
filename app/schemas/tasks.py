from pydantic import BaseModel
from datetime import datetime
from app.schemas.task_enums import TaskPriority, TaskStatus


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    priority: TaskPriority = TaskPriority.MEDIUM


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    priority: TaskPriority | None = None
    status: TaskStatus | None = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    priority: TaskPriority
    status: TaskStatus
    created_at: datetime
    updated_at: datetime