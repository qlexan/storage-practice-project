from utils.storage import new_session
from .schemas import Item, Slot, Shelf, SlotItem
from sqlmodel import select


class InventoryController:
    
    """Item functions"""
    
    def delete_item(self, id: int):
     
            with new_session() as session:
                item = session.get(Item, id)
                if item is None:
                    raise ValueError("Item doesnt exist")
                session.delete(item)
                session.commit()
        

    def add_item(self, item_added: Item):
        with new_session() as session:
            session.add(item_added)
            session.commit()
            

    def update_item(self, id: int, item_update: Item):

        with new_session() as session:
            item = session.exec(select(Item).where(Item.id == id)).first()
            if item is None:
                raise ValueError(f"Item doesnt exist")
            item.name = item_update.name
            item.supplier = item_update.supplier
            session.add(item)
            session.commit()
        

    def show_all_items(self):
        with new_session() as session:
            items = session.get(Item)
            for item in items:
                return item
            session.commit()
            
    def show_item(self, id: int):
        with new_session() as session:
            item = session.get(Item, id)
            session.commit()
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
            session.add(slotitem)
            session.commit()
            
    
    """ Slot functions"""
    
        
    def slot_belongs_to_shelf(self, slot: Slot, shelf_name: str) -> bool:
        if slot.slot_name is None:
            raise TypeError("Slot name is None")
        return slot.slot_name[0] == shelf_name
    
    """ Shelf functions """
    
    def shelf_create(self, shelf_name: str):
        
        with new_session() as session:
            shelf = Shelf(name=shelf_name)
            session.add(shelf)
            session.commit()
            
    def shelf_add_slot(self, shelf_id: int):
        with new_session() as session:
            shelf = session.get(Shelf, shelf_id)
            if shelf is None:
                raise ValueError("Shelf doesnt exist")
            
            slot_name = f"{shelf.name}{len(shelf.slots) + 1}"
            slot = Slot(slot_name=slot_name, shelf=shelf)
            shelf.slots.append(slot)
            session.add(shelf)
            session.commit()
        
    def show_shelf(self, shelf_id: int):
        with new_session() as session:
            shelf = session.get(Shelf, shelf_id)
            session.commit()
            return shelf
        
            
    def delete_shelf(self, shelf_id: int):
        with new_session() as session:
            shelf = session.get(Shelf, shelf_id)
            if shelf is None:
                raise ValueError("Shelf does not exist")
            session.delete(shelf)
            session.commit()
        
            
                
                                
    def show_shelves(self):
        with new_session() as session:
            shelves = session.get(Shelf)
            for shelf in shelves:
                return shelf
            session.commit()
    
        
    def delete_slot(self, slot_id: int):
        with new_session() as session:
            slot = session.get(Slot, slot_id)
            if slot is None:
                raise ValueError("Slot does not exist")
            session.delete(slot)
            session.commit()
            
            
        
    def get_slot(self, slot_id: int):
        with new_session() as session:
            slot = session.get(Slot, slot_id)
            if slot is None:
                raise ValueError("Slot does not exist")
            session.commit()
            return slot