from .states import State
from .transitions import *
from .registry import registry

class StateMachine:
    
    def __init__(self, current_state: State):
        self.state = current_state
        
    
    def trigger(self, target_name: str):
        
        action = self.state.transitions.get(target_name)    
        
        if target_name in self.state.allowed_classes:
            self.state.on_exit()
            if action:
                action()
            self.state = registry[target_name]
            self.state.on_enter()
        else:
            print(f"Cannot go from {self.state.name} to {target_name}")