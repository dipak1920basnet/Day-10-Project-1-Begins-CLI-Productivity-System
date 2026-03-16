# task logic

tasks = []

def add_task(title):
    task_id = len(tasks) + 1
    task = {
        "id": task_id,
        "title": title,
        "completed": False
    }
    tasks.append(task)


def get_tasks():
    return tasks


def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True


def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]