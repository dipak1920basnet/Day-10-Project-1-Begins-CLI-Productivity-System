# program contorller
import argparse
from logger import log_action
from task_manager import add_task, get_tasks, complete_task, delete_task, tasks
from storage import save_tasks, load_tasks
from display import show_tasks
from util import is_duplicate, valid_priority, sort_task, search_key_word

tasks.extend(load_tasks())

parser = argparse.ArgumentParser(description="TaskFlow - CLI Productivity Manager")

parser.add_argument("command")
parser.add_argument("value", nargs="?")
parser.add_argument("priority", nargs="?")

args = parser.parse_args()

if args.command == "add":
    print(args)
    add_task(args.value, args.priority)
    log_action("Task added")

elif args.command == "list":
    show_tasks(get_tasks())

elif args.command == "complete":
    try:
        task_id = int(args.value)
        complete_task(task_id)
    except ValueError:
        print("Invalid task ID")

elif args.command == "delete":
    delete_task(int(args.value))
    save_tasks(tasks)
    log_action("task deleted")

elif args.command == "search":
    print(args)
    print("value:: ",args.value)
    show_tasks(search_key_word(tasks,args.value))

save_tasks(tasks)
















# def menu():

#     print("\nTaskFlow CLI")
#     print("1. Add Task")
#     print("2. View Tasks")
#     print("3. Complete Task")
#     print("4. Delete Task")
#     print("5. Sort Task")
#     print("6. Search by keyword")
#     print("7. Exit")


# def main():

#     tasks.extend(load_tasks())

#     while True:

#         menu()

#         choice = input("Choose option: ")

#         if choice == "1":

#             title = input("Enter task: ")

#             # prevent duplicate tasks
#             if not is_duplicate(tasks, title):
#                 while True:
#                     print("Priority Order")
#                     print("High")
#                     print("Medium")
#                     print("Low")
#                     print("Exit")
#                     print("Enter Exit to save without priority")
#                     priority = input("Enter task priority:")

#                     if valid_priority(priority) or priority.lower() == "exit":
#                         break
#                     print("Priority must be from one of the priority order")
#                 if priority == "exit":
#                     priority = None
#                 add_task(title, priority)
#             else:
#                 print("Task already exists")

#         elif choice == "2":

#             show_tasks(get_tasks())

#         elif choice == "3":

#             task_id = int(input("Enter task ID: "))
#             complete_task(task_id)

#         elif choice == "4":

#             task_id = int(input("Enter task ID: "))
#             delete_task(task_id)

#         elif choice == "5":
#             sort_task(tasks)

#         elif choice == "6":
#             key_word = input("Enter keyword: ")
#             # print(tasks)
#             found = search_key_word(tasks, key_word)
#             if found:
#                 for i in found:
#                     print(i)
#             else:
#                 print("Keyword not found")
#         elif choice == "7":

#             save_tasks(tasks)
#             print("Tasks saved.")
#             break


# if __name__ == "__main__":
#     main()