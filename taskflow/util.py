# check duplicate
def is_duplicate(tasks, new_title):
    for i in tasks:
        if i["title"] == new_title:
            return True
    return False


# check order
def valid_priority(priority: str):
    if priority.lower() not in ["high", "medium", "low"]:
        return False
    return True


# sort task by status incomplete first
def sort_task(tasks):
    return tasks.sort(key=lambda x: x["completed"])


# search task by keyword
def search_key_word(tasks, keyword):
    found = []
    # print(tasks)
    for i in tasks:
        if keyword in i["title"]:
            found.append(i)
    return found


def stats(tasks):
    total_task = 0
    completed = 0
    remaining = 0
    for i in tasks:
        total_task += 1
        if i["completed"] == False:
            remaining += 1
        else:
            completed += 1

    data = {
        "Total tasks": total_task,
        "Completed": completed,
        "Remaining": remaining,
        "Completion Rate": f"{(completed/total_task)*100}%",
    }
    return data
