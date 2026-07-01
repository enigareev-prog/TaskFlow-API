from fastapi import APIRouter, HTTPException

from app.services.tasks_service import (
    create_task,
    get_all_tasks,
    get_task_by_id,
    update_task,
    delete_task_by_id,
)
from app.schemas.tasks import TaskCreate, TaskUpdate

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)


@router.patch("/{task_id}")
def update_task_endpoint(task_id: int, task_data: TaskUpdate):
    update_data = task_data.model_dump(exclude_unset=True)
    
    task = update_task(
        task_id=task_id,
        update_data=update_data,
    )

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return task


@router.get("")
def get_tasks():
    return get_all_tasks()


@router.post(
        "",
        summary="Create task",
        description=(
            "Creates a new task. "
            "The client must provide title. "
            "Description is optional. "
            "Priority must be one of: 'low', 'medium', 'high'. "
            "The system automatically sets id, status, created_at and updated_at."
        )
)
def create_task_endpoint(task_data: TaskCreate):
    return create_task(
        title=task_data.title,
        description=task_data.description,
        priority=task_data.priority,    
    )


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