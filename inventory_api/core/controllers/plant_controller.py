from fastapi import APIRouter, status

from core.utils.response_handler import response_handler
from core.models.entities.plant import Plant
from core.models.schemas.plant import PlantCreate, PlantUpdate, PlantRead
from core.services.plant_service import SPlantDependency

route = APIRouter()

@route.post("/{product_id}", status_code=201)
async def create_plant(product_id:int,  plant_data: PlantCreate, plant_service: SPlantDependency):
    return await response_handler(plant_service.create(product_id,plant_data))

@route.put("/{plant_id}", status_code=200)
async def update_plant(plant_id: int, plant: PlantUpdate, plant_service: SPlantDependency):
    return await response_handler(plant_service.update(plant_id, plant))

@route.get("/",status_code=200)
async def list_plant(plant_service: SPlantDependency):
    return await response_handler(plant_service.get_all())

@route.delete("/plant/{plant_id}", status_code=200)
async def delete_plant(plant_id: int, plant_service: SPlantDependency):
    return await response_handler(plant_service.delete(plant_id))
