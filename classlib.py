import os
import json
import storage

class Item():

    def __init__(self, name: str, stock: int, supplier: str, id: int = None):
        self.id = id
        self.name = name
        self.stock = stock
        self.supplier = supplier

    def to_dict(self):
        return {self.id :{
                "name": self.name,
                "stock": self.stock,
                "supplier": self.supplier}}



