from typing import Optional

class Item():

    def __init__(self, name: str, supplier: str, id: Optional[int] = None):
        self.id = id
        self.name = name
        self.supplier = supplier

    def to_dict(self):
        return {self.id: {
                "name": self.name,
                "supplier": self.supplier}}