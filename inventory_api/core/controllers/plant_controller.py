from fastapi import APIRouter, status

from core.models.entities.plant import Plant
from core.models.schemas.plant import PlantCreate, PlantUpdate
from core.services.plant_service import SPlantDependency

route = APIRouter()

@route.post("/", response_model=Plant)
async def create_plant(
    plant: PlantCreate,
    plant_service: SPlantDependency
    ):
    return plant_service.newPlant(plant)

@route.put("/{plant_id}", response_model=Plant, status_code=status.HTTP_201_CREATED)
async def update_plant(plant_id: int, plant: PlantUpdate, plant_service: SPlantDependency):
    return plant_service.update_plant(plant_id, plant)

@route.get("/", response_model= list[Plant])
async def list_plant(plant_service: SPlantDependency):
    return plant_service.list_plant()

@route.delete("/plant/{plant_id}")
async def delete_plant(plant_id: int, plant_service: SPlantDependency):
    return plant_service.delete_plant(plant_id)