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
        plant_db = Plant.model_validate(plant_data.model_dump())
        self.db.add(plant_db)
        self.db.commit()
        self.db.refresh(plant_db)
        return plant_db
    
    def list_plant(self):
        plants = self.db.exec(select(Plant)).all()
        return plants
    
    def update_plant(self, id: int, plant_data: PlantUpdate):
        plant_db = self.db.get(Plant, id)
        if plant_db == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Plant doesn't exist")
        plant_data_dict = plant_data.model_dump(exclude_unset=True)
        plant_db.sqlmodel_update(plant_data_dict)
        self.db.add(plant_db)
        self.db.commit()
        self.db.refresh(plant_db)
        return plant_db
    
    def delete_plant(self, id: int):
        plant_db = self.db.get(Plant, id)
        if plant_db == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Plant doesn't exist")
        self.db.delete(plant_db)
        self.db.commit()
        return {"message": "Plant deleted", "status": "success"}
    
SPlantDependency = Annotated[PlantService, Depends(PlantService)]