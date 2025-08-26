
def transition(target_name: str):
    def decorator(func):
        func._transition_target = target_name
        return func
    return decorator

    
    