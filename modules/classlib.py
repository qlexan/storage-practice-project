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
    def __init__(self, id: int, stock: int):
        self.id = id
        self.stock = stock
        
    def to_slot(self):
        slot = assigned_shelf + shelf_calc()
        return {slot : {
            self.id,
            self.stock
        }}
        
        
    def assign_item(self, item_id):
        if item_id != self.id:
            return False
        else:
            self.id = item_id
    
    
        
        


