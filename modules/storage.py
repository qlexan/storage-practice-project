import os
import json
from classlib import Item


_file_dir = "db.json"


def setup():
    # Create the file if it doesn't exist or is empty
    if not os.path.exists(_file_dir) or os.path.getsize(_file_dir) == 0:
        with open(get_file_dir(), "w") as f:
            json.dump({}, f)  # Correct: object first, file 

def get_file_dir():
    if not os.path.exists(_file_dir):
        raise Exception(f"{get_file_dir()} does not exist")
    return _file_dir


def set_file_dir(new_path):
    if not os.path.exists(new_path):
        raise Exception(f"{new_path} is not a valid path")
    new_path = get_file_dir()

file_dir = property(get_file_dir, set_file_dir)


def add_item_json(item):
    try:
        db = get_db()
        db.update(item)
        with open(get_file_dir(), 'w') as f:
            json.dump(db, f, indent=4)
    except Exception as e:
        raise e(f"{e}")


def get_db():
    with open(get_file_dir(), 'r') as f:
        return json.load(f)


def delete_item(id):
    try:
        data = get_db()
        data = [item for item in data if item['id'] != id]
        with open(get_file_dir(), 'w') as f:
            json.dump(data, f, indent=4)
        return f"item with id: '{id}' was succesfully removed"
    except:
        raise Exception("Item was not found")


def update_item(id, item_update):
    try:
            data = get_db()
            data[id] = Item.to_dict(item_update)        
            with open(get_file_dir(), 'w') as f:
                json.dump(data, f, indent=4)
            return f"Item with ID '{id}' was successfully updated."
    except Exception as e:
        raise e("Item was not found")

def save_db(data):
    with open(get_file_dir(), 'w') as f:
        json.dump(data, f, indent=4)