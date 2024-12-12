from fastapi import APIRouter

from core.models.schemas.order import OrderCreate

from core.services.order_service import SOrderDependency

from core.utils.response_handler import response_handler

route = APIRouter()

@route.get("/", status_code=200)
async def get_all_orders(order_service: SOrderDependency):
  return await response_handler(order_service.get_all())

@route.get("/{id}", status_code=200)
async def get_order(id: int, order_service: SOrderDependency):
  return await response_handler(order_service.get_by_id(id))
  
@route.post("/", status_code=201)
async def create_order(order: OrderCreate, order_service: SOrderDependency):
  return await response_handler(order_service.create(order))

@route.post("/{id}", status_code=200)
async def process_order(order_service: SOrderDependency):
  return await response_handler(order_service.process())

@route.put("/{id}", status_code=200)
async def update_order(id: int, order: OrderCreate, order_service: SOrderDependency):
  return await response_handler(order_service.update(id, order))

@route.delete("/{id}", status_code=200)
async def delete_order(id: int, order_service: SOrderDependency):
  return await response_handler(order_service.delete(id))
