import os
from enum import Enum

class Status(Enum):
    todo = 'todo'
    started = 'started'
    completed = 'completed'


def delete_db(db_path: str) -> None:
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"{db_path} has been deleted.")
    else:
        print(f"{db_path} does not exist.")
