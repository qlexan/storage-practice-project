from sqlmodel import SQLModel, Field, Relationship


class Item(SQLModel, table=True):

    id:int | None = Field(default=None, primary_key=True)
    name: str = Field( max_length=50)
    supplier: str = Field(max_length=50)
    slot_links: list["SlotItem"] = Relationship(back_populates="item")
    
class Slot(SQLModel, table=True):
    
    id: int | None = Field(default=None, primary_key=True)
    slot_name: str 
    shelf_id: int = Field(foreign_key="shelf.id")
    shelf: "Shelf" = Relationship(back_populates="slots")
    item_links: list["SlotItem"] = Relationship(back_populates="slot")
    
class Shelf(SQLModel, table=True):
    
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(default=str, max_length=2)
    slots: list["Slot"] = Relationship(back_populates="shelf")
    
class SlotItem(SQLModel, table=True):
    
    id : int | None = Field(default=None, primary_key=True)
    slot_id: int = Field(foreign_key="slot.id", primary_key=True)
    item_id: int = Field(foreign_key="item.id", primary_key=True)
    stock: int = Field(default=0)
    
    slot: Slot = Relationship(back_populates="items")
    item: Item = Relationship(back_populates="slot_links")