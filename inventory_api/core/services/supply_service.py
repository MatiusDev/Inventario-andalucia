from typing import Annotated
from fastapi import Depends, HTTPException
from config.db_adapter import DBSession
from sqlmodel import select

from models.entities.product import Product
from models.entities.supply import Supply
from models.enums.product import ProductType
from models.schemas.supply import SupplyCreate, SupplyRead, SupplyUpdate


class SupplyService:
	def __init__(self, db: DBSession) -> None:
		self.db = db

	async def create(self, product_id: int, supply: SupplyCreate):
		try:
			supply_db = Supply.model_validate(supply.create_dump())
			supply_db.product_id = product_id
			product_db = self.db.get(Product, product_id)
			if product_db is None:
				return {
					"status_code": 404,
					"detail": "El producto no existe",
					"status": "fail",
				}

			if product_db.type != ProductType.SUPPLY.value:
				return {
					"status_code": 400,
					"detail": "No puedes agregar este tipo de producto en insumos",
					"status": "fail",
				}

			self.db.add(supply_db)
			self.db.commit()
			self.db.refresh(supply_db)
			supply_read = SupplyRead.from_db(supply_db)
			print("HEREEEEEEEEEEEEE", supply_db)
			return {"data": supply_read, "status": "success"}
		except Exception as err:
			self.db.rollback()
			return { "status_code": 500, "detail": str(err), "status": "error" }

	def get_all(self):
		supplies = self.db.exec(select(Supply)).all() or []
		return { "data" : supplies, "status": "success" }

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