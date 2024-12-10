from typing import Annotated
from fastapi import Depends, HTTPException, status

from config.db_adapter import DBSession

from sqlmodel import select

from models.entities.plant import Plant
from models.schemas.plant import PlantCreate, PlantUpdate

class PlantService:
    def __init__(self, db: DBSession) -> None:
        self.db = db

    def newPlant(self, plant_data: PlantCreate):
        try:
            plant_db = Plant.model_validate(plant_data.model_dump())
            self.db.add(plant_db)
            self.db.commit()
            self.db.refresh(plant_db)
            return { "data" : plant_db, "status": "success" }
        except Exception as err:
            return {  "status_code": 500, "detail": str(err), "status": "error" }
        

    async def list_plant(self):
        try:
            plants = self.db.exec(select(Plant)).all()
            return { "data": plants, "status": "success"}
        except Exception as err:
            return {  "status_code": 500, "detail": str(err), "status": "error" }
        

    async def update_plant(self, id: int, plant_data: PlantUpdate):
        try:
            plant_db = self.db.get(Plant, id)

            if plant_db == None:
                return { "status_code": 404, "detail": "Plant not found", "status": "fail" }
            
            plant_data_dict = plant_data.model_dump(exclude_unset=True)
            plant_db.sqlmodel_update(plant_data_dict)
            self.db.add(plant_db)
            self.db.commit()
            self.db.refresh(plant_db)
            return { "data": plant_db, "status": "success"}
        
        except Exception as err:
            return {  "status_code": 500, "detail": str(err), "status": "error" }


    def delete_plant(self, id: int):
        try:
            plant_db = self.db.get(Plant, id)
            if plant_db == None:
                return { "status_code": 404, "detail": "Plant not found", "status": "fail" }
            self.db.delete(plant_db)
            self.db.commit()

            return {"message": "Plant deleted", "status": "success"}
        except Exception as err:
            return {  "status_code": 500, "detail": str(err), "status": "error" }
        
SPlantDependency = Annotated[PlantService, Depends(PlantService)]