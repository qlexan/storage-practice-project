from typing import Optional
from utils import storage

class Slot():
    def __init__(self, stock: int, item_name: Optional[str] = None, id: Optional[int] = None):
        self.id = id
        self.shelf = None
        self.stock = stock
        self.slot_name: Optional[str] = None
        self.item_name = item_name

    def to_dict(self):
        return {
            "id": self.id,
            "stock": self.stock,
            "item": self.item_name}

    @classmethod
    def from_dict(cls, slot_name, slot_data):
        """Takes slot name and slot data, feeds them into a Slot object and returns it"""
        obj_slot = cls(stock=slot_data["stock"],
                       id=slot_data["id"],
                       item_name=slot_data["item"])
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
        if self.slot_name is None:
            raise TypeError(f"{self.slot_name}")
        return self.slot_name[0] == shelf_name

    def __repr__(self):
        return f"<Slot {self.slot_name}: id= {self.id}, stock={self.stock}, item={self.item_name}>"