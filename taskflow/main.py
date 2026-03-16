# program contorller
from task_manager import add_task, get_tasks, complete_task, delete_task, tasks
from storage import save_tasks, load_tasks
from display import show_tasks


def menu():

    print("\nTaskFlow CLI")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")


def main():

    tasks.extend(load_tasks())

    while True:

        menu()

        choice = input("Choose option: ")

        if choice == "1":

            title = input("Enter task: ")
            add_task(title)

        elif choice == "2":

            show_tasks(get_tasks())

        elif choice == "3":

            task_id = int(input("Enter task ID: "))
            complete_task(task_id)

        elif choice == "4":

            task_id = int(input("Enter task ID: "))
            delete_task(task_id)

        elif choice == "5":

            save_tasks(tasks)
            print("Tasks saved.")
            break


if __name__ == "__main__":
    main()