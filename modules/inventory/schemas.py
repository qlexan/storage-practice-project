from sqlmodel import SQLModel, Field, Relationship

class SlotItem(SQLModel, table=True):
    slot_id: int = Field(foreign_key="slot.id", primary_key=True)
    item_id: int = Field(foreign_key="item.id", primary_key=True)
    stock: int = Field(default=0)

class Item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=50)
    supplier: str = Field(max_length=50)

    slots: list["Slot"] = Relationship(back_populates="items", link_model=SlotItem)

class Slot(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    slot_name: str
    shelf_id: int = Field(foreign_key="shelf.id")

    shelf: "Shelf" = Relationship(back_populates="slots")
    items: list[Item] = Relationship(back_populates="slots", link_model=SlotItem)

class Shelf(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=2)

    slots: list[Slot] = Relationship(back_populates="shelf")
