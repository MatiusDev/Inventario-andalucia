from typing import Annotated
from fastapi import Depends, HTTPException, status
from config.db_adapter import DBSession
from sqlmodel import select

from models.entities.supply import Supply
from models.schemas.supply import SupplyCreate, SupplyUpdate

class SupplyService:
    def __init__(self, db:DBSession) -> None:
        self.db = db

    def newSupply(self, supply_data: SupplyCreate):
        supply_db = Supply.model_validate(supply_data.model_dump())
        self.db.add(supply_db)
        self.db.commit()
        self.db.refresh(supply_db)
        return supply_db
    
    def list_supply(self):
        supplies = self.db.exec(select(Supply)).all() or []
        return supplies
    
    def update_supply(self, id: int, supply_data: SupplyUpdate):
        supply_db = self.db.get(Supply, id)
        if supply_db == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Supply doesn't exist")
        supply_data_dict = supply_data.model_dump(exclude_unset=True)
        supply_db.sqlmodel_update(supply_data_dict)
        self.db.add(supply_db)
        self.db.commit()
        self.db.refresh(supply_db)
        return supply_db
    
    def delete_supply(self, id: int):
        supply_db = self.db.get(Supply, id)
        if supply_db == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Supply doesn't exist")
        self.db.delete(supply_db)
        self.db.commit()
        return {"message": "Supply deleted", "status": "success"}
    
SSupplyDependency = Annotated[SupplyService, Depends(SupplyService)]