from config import MAX_TASK_LENGTH


def validate_task_title(title):
    if not title:
        raise ValueError("Task title cannot be empty")

    if len(title) > MAX_TASK_LENGTH:
        raise ValueError("Task title too long")

    return True
