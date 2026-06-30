tasks = []
next_task_id = 1


def get_all_tasks():
    return tasks


def create_task(title: str):
    global next_task_id 

    task = {
        "id": next_task_id,
        "title": title
    }

    tasks.append(task)
    next_task_id += 1

    return task


def get_task_by_id(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
        
    return None


def update_task_title(task_id: int, title: str):
    task = get_task_by_id(task_id)

    if task is None:
        return None
    
    task["title"] = title

    return task


def delete_task_by_id(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            return tasks.pop(index)
        
    return None