from typing import Annotated
from fastapi import Depends
from core.config.db_adapter import DBSession
from sqlmodel import select

from core.models.entities.product import Product
from core.models.enums.product import ProductType
from core.models.entities.plant import Plant
from core.models.schemas.plant import PlantCreate, PlantUpdate, PlantRead

class PlantService:
    def __init__(self, db: DBSession) -> None:
        self.db = db

    def create(self, product_id: int, plant_data: PlantCreate):
        try:
            product_db = self.db.get(Product, product_id)
            if product_db is None:
                return {
					"status_code": 404,
					"detail": "El producto no existe",
					"status": "fail",
				}
            if product_db.type != ProductType.PLANT.value:
                return {
					"status_code": 400,
					"detail": "No puedes agregar una planta a este tipo de producto",
					"status": "fail",
				}
            plant_db = Plant.model_validate(plant_data.create_dump())
            plant_db.product_id = product_id

            self.db.add(plant_db)
            self.db.commit()
            self.db.refresh(plant_db)
            plant_read = PlantRead.from_db(plant_db)
            return { "data" : plant_read, "status": "success" }
        except Exception as err:
            return {  "status_code": 500, "detail": str(err), "status": "error" }
        

    async def get_all(self):
        try:
            plants = self.db.exec(select(Plant)).all() or []
            return { "data": plants, "status": "success"}
        except Exception as err:
            return {  "status_code": 500, "detail": str(err), "status": "error" }
    
    async def get_by_id(self, id: int): 
        plant = self.db.get(Plant, id)
        
        if plant is None:
            return { "status_code": 404, "detail": "Planta no encontrada", "status": "fail" }
        
        read_plant = PlantRead.from_db(plant)
        return { "data": read_plant, "status": "success" }

    async def update(self, id: int, plant_data: PlantUpdate):
        try:
            plant_db = self.db.get(Plant, id)

            if plant_db == None:
                return { "status_code": 404, "detail": "Planta no encontrada", "status": "fail" }
        
            plant_db.sqlmodel_update(plant_data.update_dump())
            self.db.add(plant_db)
            self.db.commit()
            self.db.refresh(plant_db)

            read_plant = PlantRead.from_db(plant_db)
            return { "data": read_plant, "status": "success"}
        
        except Exception as err:
            self.db.rollback()
            return {  "status_code": 500, "detail": str(err), "status": "error" }


    def delete(self, id: int):
        try:
            plant_db = self.db.get(Plant, id)
            if plant_db == None:
                return { "status_code": 404, "detail": "Planta no encontrada", "status": "fail" }
            self.db.delete(plant_db)
            self.db.commit()

            return {"message": "Planta eliminada", "status": "success"}
        except Exception as err:
            self.db.rollback()
            return {  "status_code": 500, "detail": str(err), "status": "error" }
        
SPlantDependency = Annotated[PlantService, Depends(PlantService)]