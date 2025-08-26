from .slot import Slot

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


    def add_slot(self, new_slot: Slot):
        if new_slot.slot_name is None:
            raise ValueError("Slot must have a name before adding to shelf")
        if not new_slot.belongs_to_shelf(self.shelf_name):
            raise ValueError(
                f"Slot {new_slot.slot_name} does not belong to shelf {self.shelf_name}")
        self.slots[new_slot.slot_name] = new_slot
        
    def get_slot(self, slot_name: str) -> Slot | None:
        return self.slots.get(slot_name)

    def __repr__(self):
        return f"<Shelf {self.shelf_name} with {len(self.slots)} slots>"