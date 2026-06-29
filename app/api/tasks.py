from fastapi import APIRouter
from pydantic import BaseModel

from app.services.tasks_service import create_task, get_all_tasks

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)

tasks = []
next_task_id = 1


class TaskCreate(BaseModel):
    title: str


@router.get("")
def get_tasks():
    return get_all_tasks()


@router.post("")
def create_task_endpoint(task_data: TaskCreate):
    return create_task(title=task_data.title)