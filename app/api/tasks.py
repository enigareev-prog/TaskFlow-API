from webbrowser import get

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.tasks_service import (
    create_task,
    get_all_tasks,
    get_task_by_id,
    update_task_title,
    delete_task_by_id,
)

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)

tasks = []
next_task_id = 1


class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: str


@router.patch("/{task_id}")
def update_task(task_id: int, task_data: TaskUpdate):
    task = update_task_title(
        task_id=task_id,
        title=task_data.title,
    )

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return task


@router.get("")
def get_tasks():
    return get_all_tasks()


@router.post("")
def create_task_endpoint(task_data: TaskCreate):
    return create_task(title=task_data.title)


@router.get("/{task_id}")
def get_task(task_id: int):
    task = get_task_by_id(task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return task


@router.delete("/{task_id}")
def delete_task(task_id: int):
    deleted_task = delete_task_by_id(task_id)

    if deleted_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return {
        "message": "Task deleted successfully",
        "deleted_task": deleted_task,
    }