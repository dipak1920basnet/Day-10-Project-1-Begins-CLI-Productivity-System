import logging

logging.basicConfig(
    filename = "taskflow.log",
    level = logging.INFO
)

def log_action(action):
    logging.info(action)

