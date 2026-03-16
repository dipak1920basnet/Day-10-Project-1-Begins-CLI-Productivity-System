# save/load data
import json
from config import DATA_FILE


def save_tasks(tasks):

    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f)


def load_tasks():

    try:
        with open("data/tasks.json", "r") as f:
            return json.load(f)

    except FileNotFoundError:
        return []
