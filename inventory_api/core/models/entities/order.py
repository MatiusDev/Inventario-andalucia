from sqlmodel import SQLModel, Field, Relationship, text, TIMESTAMP, Column
from datetime import datetime

from models.enums.order import Status
from models.entities.order_supplier import OrderSupplier
from models.entities.order_product import OrderProduct
from models.entities.order_user import OrderUser

class Order(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  quantity: int
  description: str = Field(default=None, nullable=True)
  type: str
  status: str = Field(default=Status.PENDING.value)
  created_at: datetime = Field(sa_column=Column(
    TIMESTAMP(timezone=True),
    nullable=False,
    server_default=text("CURRENT_TIMESTAMP"),
    default=text("CURRENT_TIMESTAMP")
  ), default_factory=datetime.now)
  updated_at: datetime = Field(sa_column=Column(
    TIMESTAMP(timezone=True),
    nullable=False,
    server_default=text("CURRENT_TIMESTAMP"),
    default=text("CURRENT_TIMESTAMP")
  ), default_factory=datetime.now)
  
  suppliers: list["Supplier"] = Relationship(back_populates="orders", link_model=OrderSupplier) # type: ignore
  users: list["User"] = Relationship(back_populates="orders", link_model=OrderUser) # type: ignore
  products: list["Product"] = Relationship(back_populates="orders", link_model=OrderProduct) # type: ignore