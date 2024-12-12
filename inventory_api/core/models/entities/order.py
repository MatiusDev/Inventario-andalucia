from sqlmodel import SQLModel, Field, Relationship, text, TIMESTAMP, Column
from datetime import datetime

from core.models.enums.order import Status
from core.models.entities.order_supplier import OrderSupplier

class Order(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  quantity: int | None = Field(default=None, nullable=True)
  description: str
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
  id_user: int | None = Field(default=None, foreign_key="user.id", nullable=False)  
  
  user: "User" = Relationship(back_populates="orders") # type: ignore
  suppliers: list["Supplier"] = Relationship(back_populates="orders", link_model=OrderSupplier) # type: ignore
  products: list["OrderProduct"] = Relationship(back_populates="order") # type: ignore
