from core.fsm.fsm import StateMachine
import utils.storage as storage
from modules.inventory.schemas import Item, Slot, Shelf, SlotItem
from core.fsm.registry import registry


def main():
    storage.create_tables()
    fsm = StateMachine(registry["Dashboard"])

    
if __name__ == "__main__":
    main()