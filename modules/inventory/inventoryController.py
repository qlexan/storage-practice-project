from utils import storage
from .inventory import Item, Slot, Shelf
from interfaces.cli import *


class InventoryController:
    
    @property
    def db(self):
        return storage.get_db()
    
    @property
    def shelf_db(self):
        return storage.get_shelf()
    
    """Item functions"""
    
    def delete_item(self, id: int):
        try:
            db = self.db
            if str(id) not in db:
                raise Exception(f"{self.id} not found")
            db.pop(str(id))
            storage.save_db(db)
            print(f"item with id: '{id}' was succesfully removed")
        except:
            raise Exception("Item was not found")

    def add_item(self, item_added: Item):
        db = self.db
        new_id = len(db) + 1
        item_added.id = new_id
        db.update(item_added.to_dict())
        storage.save_db(db)
        return item_added

    def update_item(self, id: int, item_update: Item):
        try:
            db = self.db

            db.pop(str(id))

            
            item_update.id = id
            db[id] = item_update.to_dict()

            storage.save_db(db)
            return f"Item with ID '{id}' was successfully updated."
        except Exception as e:
            print(f"{e}")

    def show_all_items(self):
        for item in self.db.values():
            return item

    def show_item(self, id: int):
        if str(id) not in self.db:
            print(f"{id} does not exist")
            return
        item = self.db[str(id)]
        return item
    
    """ Slot functions"""
    def assign_item(self, item_id):
        db = storage.get_db()
        if str(item_id) not in db:
            print(f"Item with id {item_id} does not exist")
            return False
        if len(db) == 0:
            print("There are no items in the database")
            return False
        else:
            self.id = item_id
            self.item_name = db[str(item_id)]['name']
            return True
        
    def slot_belongs_to_shelf(self, slot: Slot, shelf_name: str) -> bool:
        if slot.slot_name is None:
            raise TypeError("Slot name is None")
        return slot.slot_name[0] == shelf_name
    
    """ Shelf functions """
    
    def shelf_create(self, shelf_name: str, slot_choice: str):
        shelves = self.shelf_db  
        if shelf_name in shelves:
            print(f"Shelf with name: {shelf_name} already exists")
            return
        
        shelf = Shelf(shelf_name)
        
        shelves.update(shelf.to_dict())
        storage.save_shelf(shelves)
        return shelf
    
    def shelf_add_slot(self, shelf: Shelf, stock: int, id: int):
        shelves = self.shelf_db
        slot = Slot(stock=stock, id=id)
        if not self.assign_item(slot.id):
            return
        length = len(shelves.get(shelf.shelf_name, {})) + 1
        slot.slot_name = shelf.shelf_name + str(length)
        self.add_slot(shelf, slot)
        
        shelves.update(shelf.to_dict())
        storage.save_shelf(shelves)
        
        print(f"Slot '{slot.slot_name}' added to shelf '{shelf.shelf_name}' successfully")

        
    def show_shelf(self, input: str, choice: str):
        shelf = self.shelf_db[input]
        if  shelf:
            print(f"Shelf: {input}") 
            for slots in shelf.values():
                return slots

                
                                
    def show_shelves(self):
        for shelves in self.shelf_db.keys():
            print(f" Shelf: {shelves}")
            for slots in self.shelf_db.values():
                return slots
    
    
    
    def add_slot(self, shelf: Shelf, new_slot: Slot):
        if new_slot.slot_name is None:
            raise ValueError("Slot must have a name before adding to shelf")
        if not self.slot_belongs_to_shelf(new_slot, shelf.shelf_name):
            raise ValueError(
                f"Slot {new_slot.slot_name} does not belong to shelf {shelf.shelf_name}")
        shelf.slots[new_slot.slot_name] = new_slot
        
    def get_slot(self,shelf: Shelf, slot_name: str) -> Slot | None:
        return shelf.slots.get(slot_name)