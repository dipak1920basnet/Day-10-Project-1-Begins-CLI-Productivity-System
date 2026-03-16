def is_duplicate(tasks, new_title):
    for i in tasks:
        if i["title"] == new_title:
            return True
    return False