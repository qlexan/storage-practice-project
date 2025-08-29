from .states import State
from .transitions import *
from .registry import registry

class StateMachine:
    
    def __init__(self, current_state: State):
        self.state = current_state
        self.state.on_enter(self)
    
    def trigger(self, state_name: str):
        
        action = self.state.transitions.get(state_name)    
        
        if state_name in self.state.allowed_classes:
            self.state.on_exit()
            if action:
                action()
            self.state = registry[state_name]
            self.state.on_enter(self)
        else:
            print(f"Cannot go from {self.state.name} to {state_name}")
    
    