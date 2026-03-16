from taskflow.task_manager import add_task, get_tasks


def test_add_task():
    add_task("Test Task")

    tasks = get_tasks()

    assert tasks[-1]["title"] == "Test Task"
