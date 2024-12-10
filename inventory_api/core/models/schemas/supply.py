from datetime import date, datetime
from enum import Enum

# from pydantic import field_validator
from sqlmodel import SQLModel, Field

from models.entities.supply import Supply
from models.enums.supply import TypeSupply, TYPE_SUPPLY_BY_ID
from datetime import datetime


class SupplyBase(SQLModel):
	unit_measure: str
	unit_quantity: int

class SupplyRead(SupplyBase):
	id: int | None
	type: str
	expiry_date: str

	@staticmethod
	def from_db(supply: Supply):
		return SupplyRead(
			id=supply.id,
			type=supply.type,
			unit_measure=supply.unit_measure,
			unit_quantity=supply.unit_quantity,
			expiry_date=supply.expiry_date.isoformat(),
		)


class SupplyCreate(SupplyBase):
	type_id: int
	expiry_date: str | None

	def create_dump(self):
		if self.expiry_date == None or self.expiry_date == "":
			self.expiry_date = None
		else:
			self.expiry_date = datetime.strptime(self.expiry_date, "%d/%m/%Y").isoformat()
   
		supply_type = TypeSupply(TYPE_SUPPLY_BY_ID.get(self.type_id)).value
		self.type_id = None
		supply = self.model_dump(exclude_unset=True)
		return {
			**supply,
			"type": supply_type,
		}

class SupplyUpdate(SupplyBase):
	pass
