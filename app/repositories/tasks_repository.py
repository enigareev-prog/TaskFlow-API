from datetime import datetime, timezone
from app.models.task import Task


tasks = []
next_task_id = 1


def get_all_tasks():
    return tasks


def create_task(title: str, description: str | None = None, priority: str = "medium"):
    global next_task_id 

    now = datetime.now(timezone.utc)

    task = Task(
        id=next_task_id,
        title=title,
        description=description,
        status="todo",
        priority=priority,
        created_at=now,
        updated_at=now,
    )

    tasks.append(task)
    next_task_id += 1

    return task


def get_task_by_id(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
        
    return None


def update_task(task_id: int, update_data: dict):
    task = get_task_by_id(task_id)

    if task is None:
        return None
    
    task.update(update_data)

    return task


def delete_task_by_id(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            return tasks.pop(index)
        
    return None