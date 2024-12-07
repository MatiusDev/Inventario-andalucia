from sqlmodel import SQLModel

from models.entities.order import Order

class OrderBase(SQLModel):
  quantity: int
  description: str | None
  type: str

class OrderCreate(OrderBase):
  pass

class OrderRead(OrderBase):
  id: int | None
  status: str
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
  status: str | None
  updated_at: str | None
