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
    def __init__(self, stock: int, id: Optional[int] = None):
        self.id = id
        self.shelf = None
        self.stock = stock
        self.slot = None

    def to_dict(self):
        return {self.slot: {
            "id": self.id,
            "stock": self.stock}
        }
    @classmethod
    def from_dict(cls, slot_dict):
        slot_name, slot_data = next(iter(slot_dict.items()))
        slot = cls(stock=slot_data["stock"], id=slot_data["id"])
        slot.slot = slot_name
        
    def assign_item(self, item_id):
        db = storage.get_db()
        if str(item_id) not in db:
            return False
        else:
            self.id = item_id
            return True

    def belongs_to_shelf(self, shelf_name: str) -> bool:
        return self.slot[0] == shelf_name

    def __repr__(self):
        return f"<Slot {self.slot}: id= {self.id}, stock={self.stock}>"


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

    def add_slot(self, slot: Slot):
        if not slot.belongs_to_shelf(self.shelf_name):
            raise ValueError(
                f"Slot {slot.slot} does not belong to shelf {self.shelf_name}")
        self.slots[slot.slot] = {"id": slot.id,
                                 "stock": slot.stock}

    def get_slot(self, slot_name: str) -> Slot | None:
        return self.slots.get(slot_name)

    def __repr__(self):
        return f"<Shelf {self.shelf_name} with {len(self.slots)} slots>"
