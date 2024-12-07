from typing import Annotated
from fastapi import Depends
# Dependencias
from config.db_adapter import DBSession

from sqlmodel import select
# Entidades y esquemas
from models.entities.order import Order
from models.entities.product import Product
from models.entities.user import User
from models.entities.order_user import OrderUser
from models.entities.supplier import Supplier

from models.schemas.order import OrderBase, OrderCreate, OrderRead

class OrderService:
  def __init__(self, db: DBSession) -> None:
    self.db = db
    
  async def get_all(self):
    # orders = self.db.exec(select(Order)).all() or []
    orders_db = self.db.exec(select(Order, User).join(OrderUser, onclause=(OrderUser.id_order == Order.id)).join(User, onclause=(OrderUser.id_user == User.id))).all() or []
    
    # orders = [{ "id": order.id, "user": user.username } for order, user in orders_db]
    # for order, order_user, user in orders_db:
    #   print(order, order_user, user)
    print("HEREEEEEEEEEEEEE", orders_db)
    
    return { "data" : "Reading orders", "status": "success" }
  
  async def get_by_id(self, id: int):
    order = self.db.get(Order, id)
    
    if order == None:
      return { "status_code": 404, "detail": "Order not found", "status": "fail" }
    
    read_order = OrderRead.model_validate(order)
    return { "data": read_order, "status": "success"}
  
  async def create(self, order: OrderCreate):
    order_db = Order.model_validate(order)
    self.db.add(order_db)
    self.db.commit()
    self.db.refresh(order_db)
    
    read_order = OrderRead.from_db(order_db)
    return { "data": read_order, "status": "success" }
  
  async def update(self, id: int, order: OrderBase):
    pass
  
  async def delete(self, id: int):
    pass
  
SOrderDependency = Annotated[OrderService, Depends(OrderService)]