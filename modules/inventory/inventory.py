from typing import Optional

class Item:

    def __init__(self, name: str, supplier: str, id: Optional[int] = None):
        self.id = id
        self.name = name
        self.supplier = supplier

    def to_dict(self):
        return {self.id: {
                "name": self.name,
                "supplier": self.supplier}}
        

class Slot:
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

    def __repr__(self):
        return f"<Slot {self.slot_name}: id= {self.id}, stock={self.stock}, item={self.item_name}>"
        
        
class Shelf:
    def __init__(self, shelf_name: str):
        self.shelf_name = shelf_name
        self.slots: dict[str, Slot] = {}

    def to_dict(self):
        """Returns Shelf object as a dictionary, i used a dict comprehension to iterate over the data"""
        return {self.shelf_name: {
                    slot_name: slot.to_dict()
                    for slot_name, slot in self.slots.items()
                }
            }

    @classmethod
    def from_dict(cls, shelf_dict, shelf_name):
        """Returns Shelf object from dictionary, feeding each slot into the shelf with a for loop"""
        shelf = cls(shelf_name)

        for slot_name, slot_data in shelf_dict[shelf_name].items():
            shelf.slots[slot_name] = Slot.from_dict(slot_name, slot_data)
        return shelf

    def __repr__(self):
        return f"<Shelf {self.shelf_name} with {len(self.slots)} slots>"
    


