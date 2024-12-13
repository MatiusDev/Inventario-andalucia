from sqlmodel import SQLModel, Field, Relationship

from core.models.entities.order_supplier import OrderSupplier

class Supplier(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  name: str
  email: str
  address: str
  phone: str | None = Field(default=None, nullable=True)
  city: str
  active: bool = Field(default=True)
  
  orders: list["Order"] = Relationship(back_populates="suppliers", link_model=OrderSupplier) # type: ignore