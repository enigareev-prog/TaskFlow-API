from fastapi import APIRouter, HTTPException

from app.services.tasks_service import (
    create_task,
    get_all_tasks,
    get_task_by_id,
    update_task,
    delete_task_by_id,
)
from app.schemas.tasks import TaskCreate, TaskUpdate, TaskResponse

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)


@router.post("",
    response_model=TaskResponse,
    summary="Create task",
    description=(
        "Creates a new task. "
        "The client must provide title. "
        "Description is optional. "
        "Priority must be one of: 'low', 'medium', 'high'. "
        "The system automatically sets id, status, created_at and updated_at."
    ),
)
def create_task_endpoint(task_data: TaskResponse):
    task = create_task(
        title=task_data.title,
        description=task_data.description,
        priority=task_data.priority,  
    )

    return task.to_dict()


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    task = get_task_by_id(task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return task.to_dict()


@router.patch("/{task_id}", response_model=TaskResponse)
def update_task_endpoint(task_id: int, task_data: TaskUpdate):
    update_data = task_data.model_dump(exclude_unset=True)

    task = update_task(
        task_id=task_id,
        update_data=update_data,
    )

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return task.to_dict()


@router.get("", response_model=list[TaskResponse])
def get_tasks():
    tasks = get_all_tasks()
    return [task.to_dict() for task in tasks]


@router.delete("/{task_id}")
def delete_task(task_id: int):
    deleted_task = delete_task_by_id(task_id)

    if deleted_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return {
        "message": "Task deleted successfully",
        "deleted_task": deleted_task.to_dict(),
    }