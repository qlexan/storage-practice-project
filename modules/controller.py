import time
from . import storage
from .classlib import Item, Slot, Shelf
from . import CLI
import sys


class Controller:

    def __init__(self):
        pass
    
    def shelf_create(self,shelf: Shelf):
        db = storage.get_shelf()
        if shelf.shelf_name not in db:
            db.update(shelf.to_dict())
            storage.save_shelf(db)
        else:
            return f"Shelf with name: {shelf.shelf_name} already exists"
    
    def shelf_add_slot(self, slot: Slot, shelf: Shelf, id):
        db = storage.get_shelf()
        if slot.assign_item(id):
            ...
    
    
    def delete_item(self):
        try:
            id = CLI.cli_id()
            db = storage.get_db()
            if str(id) not in db:
                raise Exception(f"{id} not found")
            db.pop(str(id))
            storage.save_db(db)
            print(f"item with id: '{id}' was succesfully removed")
        except:
            raise Exception("Item was not found")

    def add_item(self):
        item_added = CLI.cli_add()
        db = storage.get_db()
        db_len = len(db)
        new_id = db_len + 1 if db_len > 0 else 1
        item_added.id = new_id
        db.update(item_added.to_dict())
        storage.save_db(db)
        return item_added

    def update_item(self):
        try:
            id = CLI.cli_id()
            db = storage.get_db()

            db.pop(str(id))

            item_update = CLI.cli_add()
            item_update.id = id
            db[id] = item_update.to_dict()

            storage.save_db(db)
            return f"Item with ID '{id}' was successfully updated."
        except Exception:
            raise Exception("Item was not found")

    def show_all_items(self):
        db = storage.get_db()
        for item in db.values():
            CLI.cli_show(item)

    def show_item(self):
        id = CLI.cli_id()
        data = storage.get_db()
        if str(id) not in data:
            print(f"{id} does not exist")
            return
        item = data[str(id)]
        CLI.cli_show(item)

    def quit_out(self):
        print("Goodbye")
        sys.exit()
        
    def show_main(self):
        while True:
            choice = CLI.cli_main()
            commands = self.get_commands()
            action = commands.get(choice)
            if action:
                try:
                    action()
                except Exception as e:
                    CLI.cli_error(e)
            
            input("\nPress enter to continue...")

    def get_commands(self):
        return {
            1: self.add_item,
            2: self.delete_item,
            3: self.update_item,
            4: self.show_item,
            5: self.show_all_items,
            0: self.quit_out
        }
