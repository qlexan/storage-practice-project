
from .transitions import *
from interfaces.cli import *

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
        

class Dashboard(State):
    
    allowed_classes =  ["Inventory", "Shelves","Slots", "Items"]
    
    def __init__(self):
        super().__init__("Dashboard")
    
    @transition("Inventory")    
    def inventory(self):
        print("Entering inventory from Dashboard")
        
    @transition("Shelves")    
    def shelves(self):
        print("Entering Shelves from Dashboard")
        
    @transition("Slots")    
    def slots(self):
        print("Entering Slots from Dashboard")
    
    @transition("Items")    
    def items(self):
        print("Entering Items from Dashboard")
        
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