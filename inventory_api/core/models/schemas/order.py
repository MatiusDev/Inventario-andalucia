from typing import List
from sqlmodel import SQLModel

from models.entities.order import Order
from models.schemas.product import ProductOrder
from models.enums.order import ORDER_TYPE_BY_ID

class OrderBase(SQLModel):
  description: str

class OrderCreate(OrderBase):
  id_supplier: int = -1
  type_id: int
  products: List[ProductOrder]
  
  def create_dump(self):
    if self.id_supplier == -1:
      self.id_supplier = None
    self.products = None
    order = self.model_dump(exclude_none=True)
    if order.get("type") == None:
      order["type"] = ORDER_TYPE_BY_ID.get(self.type_id)
      order.pop("type_id")
    return order

class OrderRead(OrderBase):
  id: int | None
  quantity: int | None
  status: str
  type: str
  created_at: str
  updated_at: str
  
  @staticmethod
  def from_db(order: Order):
    return OrderRead(
      id=order.id,
      quantity=order.quantity,
      description=order.description,
      type=order.type,
      status=order.status,
      created_at=order.created_at.isoformat(),
      updated_at=order.updated_at.isoformat()
    )

class OrderUpdate(OrderBase):
  id: int | None
  quantity: int | None
  status: str | None
  updated_at: str | None
  type: str
  
