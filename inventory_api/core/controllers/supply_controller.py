from fastapi import APIRouter

from core.models.schemas.supply import SupplyCreate, SupplyUpdate
from core.services.supply_service import SSupplyDependency

from core.utils.response_handler import response_handler

route = APIRouter()

@route.get("/", status_code=200)
async def list_supply(supply_service: SSupplyDependency):
    return await response_handler(supply_service.get_all())

@route.get("/{id}", status_code=200)
async def get_supply(id: int, supply_service: SSupplyDependency):
    return await response_handler(supply_service.get_by_id(id))

@route.post("/{product_id}", status_code=201)
async def create_supply(product_id: int, supply: SupplyCreate, supply_service: SSupplyDependency):
    return await response_handler(supply_service.create(product_id, supply))

@route.put("/{id}", status_code=201)
async def update_supply(id: int, supply: SupplyUpdate, supply_service: SSupplyDependency):
    return await response_handler(supply_service.update(id, supply))

@route.delete("/supply/{id}", status_code=200)
async def delete_supplies(id: int, supply_service: SSupplyDependency):
    return await response_handler(supply_service.delete(id))