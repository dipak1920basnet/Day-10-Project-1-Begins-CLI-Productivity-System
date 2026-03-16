# check duplicate
def is_duplicate(tasks, new_title):
    for i in tasks:
        if i["title"] == new_title:
            return True
    return False

# check order 
def valid_priority(priority:str):
    if priority.lower() not in ["high","medium","low"]:
        return False
    return True

def sort_task(tasks):
    return tasks.sort(key=lambda x:x["completed"])

def search_key_word(tasks, keyword):
    ...