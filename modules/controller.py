import time
from . import storage
from .classlib import Item, Slot, Shelf
from . import CLI
import sys


class Controller:

    def __init__(self):
        pass
    
    @property
    def db(self):
        return storage.get_db()
    
    @property
    def shelf_db(self):
        return storage.get_shelf()
        
    def shelf_create(self):
        shelf_name = CLI.cli_shelf()  
        if shelf_name in self.shelf_db:
            print(f"Shelf with name: {shelf_name} already exists")
            return
        
        shelf = Shelf(shelf_name, slot=None)
        slot_choice = CLI.cli_slot_choice()  # 'y' or 'n'
        if slot_choice.lower() == 'y':
            self.shelf_add_slot(shelf)
        

        self.shelf_db.update(shelf.to_dict())
        storage.save_shelf(self.shelf_db)
        print(f"Shelf '{shelf_name}' created successfully")
    
    def shelf_add_slot(self, shelf: Shelf):

        slot = CLI.cli_slot()  
        
        if not slot.assign_item(slot.id):
            print(f"Item with id {slot.id} does not exist")
            return
        
        shelf.add_slot(slot)
        
        self.shelf_db.update(shelf.to_dict())
        storage.save_shelf(self.shelf_db)
        
        print(f"Slot '{slot.slot}' added to shelf '{shelf.shelf_name}' successfully")

            
    
    
    def delete_item(self):
        try:
            id = CLI.cli_id()
            if str(id) not in self.db:
                raise Exception(f"{self.id} not found")
            self.db.pop(str(id))
            storage.save_db(self.db)
            print(f"item with id: '{id}' was succesfully removed")
        except:
            raise Exception("Item was not found")

    def add_item(self):
        item_added = CLI.cli_add()
        db_len = len(self.db)
        new_id = db_len + 1 if db_len > 0 else 1
        item_added.id = new_id
        self.db.update(item_added.to_dict())
        storage.save_db(self.db)
        return item_added

    def update_item(self):
        try:
            id = CLI.cli_id()

            self.db.pop(str(id))

            item_update = CLI.cli_add()
            item_update.id = id
            self.db[id] = item_update.to_dict()

            storage.save_db(self.db)
            return f"Item with ID '{id}' was successfully updated."
        except Exception:
            raise Exception("Item was not found")

    def show_all_items(self):
        for item in self.db.values():
            CLI.cli_show(item)

    def show_item(self):
        id = CLI.cli_id()
        if str(id) not in self.db:
            print(f"{id} does not exist")
            return
        item = self.db[str(id)]
        CLI.cli_show(item)

    def quit_out(self):
        print("Goodbye")
        sys.exit()
        
    def show_main(self):
        while True:
            choice = CLI.cli_main()
            commands = self.main_menu_options()
            action = commands.get(choice)
            if action:
                try:
                    action()
                except Exception as e:
                    CLI.cli_error(e)
            
            input("\nPress enter to continue...")

    def main_menu_options(self):
        return {
            1: self.add_item,
            2: self.delete_item,
            3: self.update_item,
            4: self.show_item,
            5: self.show_all_items,
            0: self.quit_out
        }
