from fastapi import APIRouter, status

from models.entities.supply import Supply
from models.schemas.supply import SupplyCreate, SupplyUpdate
from services.supply_service import SSupplyDependency

route = APIRouter()

@route.post("/", response_model=Supply)
async def create_supply(
    supply: SupplyCreate,
    supply_service: SSupplyDependency
    ):
    return supply_service.newSupply(supply)

@route.put("/{supply_id}", response_model=Supply, status_code=status.HTTP_201_CREATED)
async def update_supply(supply_id: int, supply: SupplyUpdate, supply_service: SSupplyDependency):
    return supply_service.update_supply(supply_id, supply)

@route.get("/", response_model= list[Supply])
async def list_supply(supply_service: SSupplyDependency):
    return supply_service.list_supply()

@route.delete("/supply/{supply_id}")
async def delete_supplies(supply_id: int, supply_service: SSupplyDependency):
    return supply_service.delete_supply(supply_id)