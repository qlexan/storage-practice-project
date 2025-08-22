import os
import json
import storage

class Item():

    def __init__(self, name: str, supplier: str, id: int = None):
        self.id = id
        self.name = name
        self.supplier = supplier

    def to_dict(self):
        return {self.id :{
                "name": self.name,
                "supplier": self.supplier}}


class Slot():
    def __init__(self, id: int, stock: int, shelf):
        self.id = id
        self.shelf = shelf
        self.stock = stock
        
    def to_slot(self):
        slot = self.shelf + self.shelf_calc()
        return {slot : {
            self.id,
            self.stock
        }}
        
        
    def assign_item(self, item_id):
        if item_id != self.id:
            return False
        else:
            self.id = item_id
            
            
class Shelf:
    def __init__(self, slot: Slot, shelf_name):
        self.shelf_name = shelf_name
        self.slot = slot
        
        
    def shelf_create(self):
        return {self.shelf_name: {self.slot}}
        
    def shelf_calc(self):
        length = len(storage.get_shelf())
        return length + 1 if length > 0 else 1
    
    
        
        


