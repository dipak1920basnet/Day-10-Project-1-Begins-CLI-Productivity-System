# save/load data
import json
from config import DATA_FILE, BACKUP_FILE
import shutil


def backup():
    shutil.copy(DATA_FILE,BACKUP_FILE)

def save_tasks(tasks):
    """
    backup the new data before saving because 
    if something worng appears while saving we can go back.
    """ 
    backup()

    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f)
    

def load_tasks():

    try:
        with open("data/tasks.json", "r") as f:
            return json.load(f)

    except FileNotFoundError:
        return []
