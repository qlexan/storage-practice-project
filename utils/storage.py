import os
import json
from config.env import DB_PATH, SHELF_PATH


def setup():
    if not os.path.exists(DB_PATH) or os.path.getsize(DB_PATH) == 0:
        with open(DB_PATH, "w") as f:
            json.dump({}, f)
    if not os.path.exists(SHELF_PATH) or os.path.getsize(SHELF_PATH) == 0:
        with open(SHELF_PATH, "w") as f:
            json.dump({}, f)

def get_db():
    with open(DB_PATH, 'r') as f:
        return json.load(f)
    
def get_shelf():
    with open(SHELF_PATH, 'r') as f:
        return json.load(f)

def save_db(data):
    with open(DB_PATH, 'w') as f:
        json.dump(data, f, indent=4)
        
def save_shelf(data):
    with open(SHELF_PATH, 'w') as f:
        json.dump(data, f, indent=4)