from fastapi import APIRouter, status

from utils.response_handler import response_handler
from models.entities.plant import Plant
from models.schemas.plant import PlantCreate, PlantUpdate, PlantRead
from services.plant_service import SPlantDependency

route = APIRouter()

@route.post("/", status_code=201)
async def create_plant(plant_data: PlantCreate, plant_service: SPlantDependency):
    return await response_handler(plant_service.newPlant(plant_data))

@route.put("/{plant_id}", status_code=200)
async def update_plant(plant_id: int, plant: PlantUpdate, plant_service: SPlantDependency):
    return await response_handler(plant_service.update_plant(plant_id, plant))

@route.get("/",status_code=200)
async def list_plant(plant_service: SPlantDependency):
    return await response_handler(plant_service.list_plant())

@route.delete("/plant/{plant_id}", status_code=200)
async def delete_plant(plant_id: int, plant_service: SPlantDependency):
    return await response_handler(plant_service.delete_plant(plant_id))