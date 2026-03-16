# save/load data
import json


def save_tasks(tasks):

    with open("data/tasks.json", "w") as f:
        json.dump(tasks, f)


def load_tasks():

    try:
        with open("data/tasks.json", "r") as f:
            return json.load(f)

    except FileNotFoundError:
        return []