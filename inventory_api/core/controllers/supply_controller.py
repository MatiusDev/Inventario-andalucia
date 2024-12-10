from fastapi import APIRouter

from models.schemas.supply import SupplyCreate, SupplyUpdate
from services.supply_service import SSupplyDependency

from utils.response_handler import response_handler

route = APIRouter()

@route.get("/", status_code=200)
async def list_supply(supply_service: SSupplyDependency):
    return await response_handler(supply_service.get_all())

@route.post("/{product_id}", status_code=201)
async def create_supply(product_id: int, supply: SupplyCreate, supply_service: SSupplyDependency):
    return await response_handler(supply_service.create(product_id, supply))

# @route.put("/{supply_id}", response_model=Supply, status_code=status.HTTP_201_CREATED)
# async def update_supply(supply_id: int, supply: SupplyUpdate, supply_service: SSupplyDependency):
#     return supply_service.update_supply(supply_id, supply)

# @route.delete("/supply/{supply_id}")
# async def delete_supplies(supply_id: int, supply_service: SSupplyDependency):
#     return supply_service.delete_supply(supply_id)