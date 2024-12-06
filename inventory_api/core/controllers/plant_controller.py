from fastapi import APIRouter, status

from models.entities.plant import Plant
from models.schemas.plant import PlantCreate, PlantUpdate, PlantRead
from services.plant_service import SPlantDependency

route = APIRouter()

@route.post("/", response_model=PlantRead, status_code=201)
async def create_plant(plant_data: PlantCreate, plant_service: SPlantDependency):
    return plant_service.newPlant(plant_data)

@route.put("/{plant_id}", response_model=Plant, status_code=200)
async def update_plant(plant_id: int, plant: PlantUpdate, plant_service: SPlantDependency):
    return plant_service.update_plant(plant_id, plant)

@route.get("/", response_model= list[Plant])
async def list_plant(plant_service: SPlantDependency):
    return plant_service.list_plant()

@route.delete("/plant/{plant_id}")
async def delete_plant(plant_id: int, plant_service: SPlantDependency):
    return plant_service.delete_plant(plant_id)