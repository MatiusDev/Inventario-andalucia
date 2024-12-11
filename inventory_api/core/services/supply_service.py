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

	async def get_all(self):
		supplies = self.db.exec(select(Supply)).all() or []
		return { "data" : supplies, "status": "success" }

	async def get_by_id(self, id: int):
		supply = self.db.get(Supply, id)

		if supply is None:
			return { "status_code": 404, "detail": "Insumo no encontrado", "status": "fail" }
 
		read_supply = SupplyRead.from_db(supply)
		return { "data": read_supply, "status": "success" }

	async def create(self, product_id: int, supply: SupplyCreate):
		try:
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
					"detail": "No puedes agregar un insumo a este tipo de producto",
					"status": "fail",
				}
			supply_db = Supply.model_validate(supply.create_dump())
			supply_db.product_id = product_id

			self.db.add(supply_db)
			self.db.commit()
			self.db.refresh(supply_db)
			supply_read = SupplyRead.from_db(supply_db)
			return { "data": supply_read, "status": "success" }
		except Exception as err:
			self.db.rollback()
			return { "status_code": 500, "detail": str(err), "status": "error" }

	async def update(self, id: int, supply: SupplyUpdate):
		try:
			supply_db = self.db.get(Supply, id)
			if supply_db == None:
				return { "status_code": 404, "detail": "Insumo no encontrado", "status": "fail" }
			supply_db.sqlmodel_update(supply.update_dump())
			self.db.add(supply_db)
			self.db.commit()
			self.db.refresh(supply_db)

			read_supply = SupplyRead.from_db(supply_db)
			return { "data": read_supply, "status": "success" }
		except Exception as err:
			self.db.rollback()
			return { "status_code": 500, "detail": str(err), "status": "error" }

	async def delete(self, id: int):
		try:
			supply_db = self.db.get(Supply, id)
			if supply_db == None:
				return { "status_code": 404, "detail": "Insumo no encontrado", "status": "fail" }
  
			self.db.delete(supply_db)
			self.db.commit()
			return { "message": "Insumo eliminado correctamente", "status": "success" }
		except Exception as err:
			self.db.rollback()
			return { "status_code": 500, "detail": str(err), "status": "error" }

SSupplyDependency = Annotated[SupplyService, Depends(SupplyService)]