import os
import json
from . import storage
from typing import Optional


class Item():

    def __init__(self, name: str, supplier: str, id: int = None):
        self.id = id
        self.name = name
        self.supplier = supplier

    def to_dict(self):
        return {self.id: {
                "name": self.name,
                "supplier": self.supplier}}


class Slot():
    def __init__(self, stock: int, item_name: Optional[str] = None, id: Optional[int] = None):
        self.id = id
        self.shelf = None
        self.stock = stock
        self.slot_name = None
        self.item_name = item_name

    def to_dict(self):
        return {self.slot_name: {
            "id": self.id,
            "stock": self.stock,
            "item": self.item_name}
        }
    @classmethod
    def from_dict(cls, slot_dict):
        slot_name, slot_data = next(iter(slot_dict.items()))
        obj_slot = cls(stock=slot_data["stock"], 
                       id=slot_data["id"], 
                       name=slot_data["item"])
        obj_slot.slot_name = slot_name
        return obj_slot
        
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

    def belongs_to_shelf(self, shelf_name: str) -> bool:
        return self.slot_name[0] == shelf_name

    def __repr__(self):
        return f"<Slot {self.slot_name}: id= {self.id}, stock={self.stock}, item={self.item_name}>"


class Shelf:
    def __init__(self, shelf_name: str):
        self.shelf_name = shelf_name
        self.slots = {}

    def to_dict(self):
        return {self.shelf_name: self.slots}

    @classmethod
    def from_dict(cls, shelf_dict, shelf_name):
        shelf = cls(shelf_name)
        
        for slot_name, slot_data in shelf_dict[shelf_name].items():
            slot_dict = {slot_name : slot_data}
            slot_obj = Slot.from_dict(slot_dict, shelf_name)
            shelf.slots[slot_name] = slot_obj

        return shelf

    def add_slot(self, new_slot: Slot):
        if not new_slot.belongs_to_shelf(self.shelf_name):
            raise ValueError(
                f"Slot {new_slot.slot_name} does not belong to shelf {self.shelf_name}")
        self.slots[new_slot.slot_name] = {
                                        "id": new_slot.id,
                                        "stock": new_slot.stock,
                                        "item": new_slot.item_name}

    def get_slot(self, slot_name: str) -> Slot | None:
        return self.slots.get(slot_name)

    def __repr__(self):
        return f"<Shelf {self.shelf_name} with {len(self.slots)} slots>"
