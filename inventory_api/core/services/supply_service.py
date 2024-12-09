from typing import Annotated
from fastapi import Depends, HTTPException
from config.db_adapter import DBSession
from sqlmodel import select

from models.enums.product import Type_Product
from models.entities.product import Product
from models.entities.supply import Supply
from models.schemas.supply import SupplyCreate, SupplyRead, SupplyUpdate

class SupplyService:
    def __init__(self, db:DBSession) -> None:
        self.db = db

    def create(self, supply_data: SupplyCreate):
        try:
            new_supply = SupplyCreate.supply_dump(supply_data)
            supply_db = Supply.model_validate(new_supply)
            product_db = self.db.get(Product, supply_data.id_product)
            if product_db is None:
                raise HTTPException(status_code=404, detail="El producto no existe")
            
            if product_db.type_product != Type_Product.INSUMO.value:
                raise HTTPException(status_code=400, detail="No puedes agregar este tipo de producto en herramientas")

            self.db.add(supply_db)
            self.db.commit()
            self.db.refresh(supply_db)
            supply_read = SupplyRead.model_validate(supply_db)
            print("HEREEEEEEEEEEEEE", supply_db)
            return supply_read 
        
        except Exception as err:
            raise HTTPException(status_code=500, detail=str(err))
    
    def get_all(self):
        supplies = self.db.exec(select(Supply)).all() or []
        return supplies
    
    # def update_supply(self, id: int, supply_data: SupplyUpdate):
    #     supply_db = self.db.get(Supply, id)
    #     if supply_db == None:
    #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Supply doesn't exist")
    #     supply_data_dict = supply_data.model_dump(exclude_unset=True)
    #     supply_db.sqlmodel_update(supply_data_dict)
    #     self.db.add(supply_db)
    #     self.db.commit()
    #     self.db.refresh(supply_db)
    #     return supply_db
    
    # def delete_supply(self, id: int):
    #     supply_db = self.db.get(Supply, id)
    #     if supply_db == None:
    #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Supply doesn't exist")
    #     self.db.delete(supply_db)
    #     self.db.commit()
    #     return {"message": "Supply deleted", "status": "success"}
    
SSupplyDependency = Annotated[SupplyService, Depends(SupplyService)]