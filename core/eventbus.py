from modules.inventory.schemas import Item, Slot, Shelf, SlotItem
from utils.storage import new_session
from sqlmodel import Session, SQLModel, select

class EventBus:
    
    """EventBus class to handle InventoryController inputs.
        It batches all CRUD into a list and then flushes on command.
    """
    def __init__(self):
        self.pending_updates = dict(list)
        self.pending_relationships = list[tuple[str, SQLModel]]  = []
    def publish(self, action: str, data=None, model_id: int | None = None):
        """Publish function that appends input to pending updates.

        Args:
            model_id (int, optional): the id of the model. If left to None it will assume the model is a relationship.
            action (str): "create", "update" or "delete" to inform the flush.
            data (_type_, optional): Is the actual Model. Defaults to None.
        """
        if model_id is not None:
            self.pending_updates[model_id].append((action, data))
        else:
            self.pending_relationships.append((action, data))
        
    def flush(self, session: Session,  model_id=None):
        """Flushing function that uses the internal flush logic defined elsewhere.

        Args:
            session (Session): Active db session
            model_id (_type_, optional): Optional input of model, otherwise just dumps all appending updates. Defaults to None.
        """
        if model_id:
                self._flush_product(session, model_id)
        else:
            for pid in list(self.pending_updates.keys()):
                self._flush_product(session, pid)
            for model in self.pending_relationships:
                self._flush_relationship(session)
        session.commit()
        
    def _flush_product(self, session: Session, model_id: int):
        
        """Logic of flushing assigned models with their assigned action.
        """
        
        updates = self.pending_updates[model_id]
        for action, data in updates:
            if action == "create":
                session.add(data)
            elif action == "delete":
                session.delete(data)
            elif action == 'update':
                if isinstance(data, SQLModel):
                    model_class = type(data)
                    pk_val = getattr(data, "id")
                    model = session.get(model_class, pk_val)
                    if model:
                        for field, value in data.model_dump(exclude_unset=True).items():
                            setattr(model, field, value)
                        session.add(model)
        self.pending_updates.clear()
        
    def _flush_relationship(self, session: Session):
        """Internal class to handle flushing of models with no ids, usually relationships

        Args:
            session (Session): The active db session
        """
        
        for action, data in self.pending_relationships:
            if action == "create":
                session.add(data)
            elif action == "update":
                existing = session.exec(
                    select(type(data)).where(
                    type(data).slot_id == data.slot_id,
                    type(data).item_id == data.item_id)).first()
 
                if existing:
                    for field, value in data.model_dump(exclude_unset=True).items():
                        setattr(existing, field, value)
                    session.add(existing)
            elif action == "delete":
                session.delete(data)
        self.pending_relationships.clear()               