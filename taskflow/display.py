# user_interface
def show_tasks(tasks):

    if not tasks:
        print("No tasks found")
        return

    print("ID   STATUS   TASK")
    print("-------------------------")

    for task in tasks:

        status = "✓" if task["completed"] else "✗"

        print(f"{task['id']}    {status}       {task['title']}")