# task logic
from taskflow.util import is_duplicate, valid_priority
from taskflow.validatory import validate_task_title

tasks = []


def add_task(title, priority=None):

    validate_task_title(title)

    if not is_duplicate(tasks, title):
        task_id = len(tasks) + 1

        task = {"id": task_id, "title": title, "completed": False}

        # Add priority to task
        if priority != None:
            if valid_priority(priority):
                task["priority"] = priority
        tasks.append(task)
    else:
        print("Task already exists")


def get_tasks():
    return tasks


def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True


def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
