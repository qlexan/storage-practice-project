
from .transitions import *
from interfaces.cli import *
from modules.inventory.inventoryController import InventoryController


invcont = InventoryController()

class State:

    allowed_classes: list[str] = []
    def __init__(self, name: str):
        self.name = name
        self.transitions: dict = {}

        
        for attr_name in dir(self):
            method = getattr(self, attr_name)
            if callable(method) and hasattr(method, "_transition_target"):
                target = method._transition_target
                self.transitions[target] = method
    
    def on_enter(self, fsm=None):
        raise NotImplementedError
    
    def on_exit(self):
        raise NotImplementedError    

class Dashboard(State):
    
    allowed_classes =  ["Inventory", "Shelves","Slots", "Items"]
    
    def __init__(self):
        super().__init__("Dashboard")
    
        
    def on_enter(self, fsm=None):
        print("In Dashboard")
        if fsm is not None:    
            state = cli_main()
            fsm.trigger(state)
        
    def on_exit(self):...

class Inventory(State):
    allowed_classes =  ["Dashboard", "Shelves", "Items"]
    
    def __init__(self):
        super().__init__("Inventory")
        
    def on_enter(self, fsm=None):
        print("In Inventory")
        
        sub_states = {
            1: self.add_item,
            2: self.show_item,
            3: self.show_all,
            4: self.update_item,
            5: self.delete_item,
            6: self.add_to_slot,
            7: lambda: fsm.trigger("Dashboard")
        }
        
        if fsm:
            while True:
                sub = cli_inventory()
                action = sub_states.get(sub)
                if action:
                    action()
                

    def add_item(self):
        item = cli_add()
        invcont.add_item(item)
    
    def show_item(self):
        id = cli_id("item")
        invcont.show_item(id)
        
    def show_all(self):
        items = invcont.show_all_items()
        cli_show(items)
        
    def update_item(self):
        id = cli_id("item")
        item = cli_add
        invcont.update_item(id, item)
        
    def delete_item(self):
        id = cli_id("item")
        invcont.delete_item(id)
        
    def add_to_slot(self):
        item_id = cli_id("item")
        slot_id = cli_id("slot")
        stock = cli_stock()
        invcont.assign_slot(item_id, slot_id, stock)
        
    def on_exit(self):...
    
class Shelves(State):
    allowed_classes = ["Inventory"]
    
    def __init__(self):
        super().__init__("Shelves")
        
    def on_enter(self, fsm=None):
        print("In Shelves")
        
    
    def on_exit(self):...
        
class Slots(State):
    allowed_classes = ["Inventory", "Shelves", "Items"]
    
    def __init__(self):
        super().__init__("Slots")
        
    def on_enter(self, fsm=None):
        print("In Slots")
        
    
    def on_exit(self):...
        

class Items(State):
    allowed_classes = ["Inventory", "Slots", "Shelves"]
    
    def __init__(self):
        super().__init__("Items")
        
    def on_enter(self, fsm=None):
        print("In Items")
        
    
    def on_exit(self):...