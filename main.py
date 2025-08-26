from core.fsm.fsm import StateMachine
import utils.storage as storage
from core.fsm.registry import registry


def main():
    storage.setup()
    fsm = StateMachine(registry["Dashboard"])
    fsm.state.on_enter()
if __name__ == "__main__":
    main()