import os
import json
from classlib import Item
from .config import DB_PATH


def setup():
    # Create the file if it doesn't exist or is empty
    if not os.path.exists(DB_PATH) or os.path.getsize(DB_PATH) == 0:
        with open(DB_PATH, "w") as f:
            json.dump({}, f)  # Correct: object first, file 


def add_item_json(item):
    try:
        db = get_db()
        db.update(item)
        with open(DB_PATH, 'w') as f:
            json.dump(db, f, indent=4)
    except Exception as e:
        raise e(f"{e}")


def get_db():
    with open(DB_PATH, 'r') as f:
        return json.load(f)


def delete_item(id):
    try:
        data = get_db()
        data = [item for item in data if item['id'] != id]
        with open(DB_PATH, 'w') as f:
            json.dump(data, f, indent=4)
        return f"item with id: '{id}' was succesfully removed"
    except:
        raise Exception("Item was not found")


def update_item(id, item_update):
    try:
            data = get_db()
            data[id] = Item.to_dict(item_update)        
            with open(DB_PATH, 'w') as f:
                json.dump(data, f, indent=4)
            return f"Item with ID '{id}' was successfully updated."
    except Exception as e:
        raise e("Item was not found")

def save_db(data):
    with open(DB_PATH, 'w') as f:
        json.dump(data, f, indent=4)