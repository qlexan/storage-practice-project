from utils.storage import new_session
from .schemas import Item, Slot, Shelf, SlotItem
from sqlmodel import select
from core.eventbus import EventBus


class InventoryController:
    
    """Controller class for the all the inventory actions"""
    def __init__(self):
        self.bus = EventBus()
    # Item functions
    
    def delete_item(self, id: int):
        
        
        with new_session() as session:
            item = session.get(Item, id)
            if item is None:
                raise ValueError("Item doesnt exist")
            self.bus.publish(id, "delete", item)
        

    def add_item(self, item_added: Item):
        with new_session() as session:
            self.bus.publish(item_added.id, "create", item_added)
            

    def update_item(self, id: int, item_update: Item):

        with new_session() as session:
            item = session.exec(select(Item).where(Item.id == id)).first()
            if item is None:
                raise ValueError(f"Item doesnt exist")
            updated_item = Item(id=id, name=item_update.name, supplier=item_update.supplier)
            self.bus.publish(id, "update", updated_item)
        

    def show_all_items(self):
        with new_session() as session:
            self.bus.flush()
            items = session.exec(select(Item)).all()
            return items

            
    def show_item(self, id: int):
        with new_session() as session:
            self.bus.flush(id)
            item = session.get(Item, id)
            return item
        
        
    def assign_slot(self, item_id: int, slot_id: int, stock: int):
        with new_session() as session:
            item = session.get(Item, item_id)
            slot = session.get(Slot, slot_id)
            if item is None:
                raise ValueError("Item is none")
            if slot is None: 
                raise ValueError("Slot is none")
            
            slotitem = SlotItem(item_id=item.id, slot_id=slot.id, stock=stock)
            self.bus.publish("create", slotitem)
            
    
    # Slot functions
    
        
    def slot_belongs_to_shelf(self, slot: Slot, shelf_name: str) -> bool:
        if slot.slot_name is None:
            raise TypeError("Slot name is None")
        return slot.slot_name[0] == shelf_name
    
    
    # Shelf functions 
    
    def shelf_create(self, shelf_name: str):
        
        with new_session() as session:
            shelves = session.exec(select(Shelf).where(Shelf.name == shelf_name)).first()
            if shelves:
                raise ValueError(f"Shelf with name: {shelf_name} already exists")
            else:
                shelf = Shelf(name=shelf_name)
                self.bus.publish(shelf.id, "create", shelf)
            
            
    def shelf_add_slot(self, shelf_id: int):
        with new_session() as session:
            shelf = session.get(Shelf, shelf_id)
            if shelf is None:
                raise ValueError("Shelf doesnt exist")
            
            slot_name = f"{shelf.name}{len(shelf.slots) + 1}"
            slot = Slot(slot_name=slot_name, shelf=shelf)
            shelf.slots.append(slot)
            self.bus.publish(shelf.id, "create", shelf)
        
    def show_shelf(self, shelf_id: int):
        with new_session() as session:
            self.bus.flush(shelf_id)
            shelf = session.get(Shelf, shelf_id)
            return shelf
        
            
    def delete_shelf(self, shelf_id: int):
        with new_session() as session:
            shelf = session.get(Shelf, shelf_id)
            if shelf is None:
                raise ValueError("Shelf does not exist")
            self.bus.publish(shelf, "delete", model_id=shelf_id)
                
                                
    def show_shelves(self):
        with new_session() as session:
            self.bus.flush()
            shelves = session.exec(select(Shelf)).all()
            return shelves
        
        
    def delete_slot(self, slot_id: int):
        with new_session() as session:
            slot = session.get(Slot, slot_id)
            if slot is None:
                raise ValueError("Slot does not exist")
            self.bus.publish(slot.id, "delete", slot)
            
               
    def get_slot(self, slot_id: int):
        with new_session() as session: 
            self.bus.flush()
            slot = session.get(Slot, slot_id)
            if slot is None:
                raise ValueError("Slot does not exist")
            return slot