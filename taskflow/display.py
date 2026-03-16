# user_interface
def show_tasks(tasks):

    if not tasks:
        print("No tasks found")
        return

    for task in tasks:

        status = "✓" if task["completed"] else " "

        print(f"[{status}] {task['id']} - {task['title']}")