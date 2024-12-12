from sqlmodel import SQLModel
from datetime import datetime

from core.models.entities.supply import Supply
from core.models.enums.supply import TypeSupply, TYPE_SUPPLY_BY_ID

class SupplyBase(SQLModel):
	unit_measure: str
	unit_quantity: int

class SupplyRead(SupplyBase):
	id: int | None
	type: str
	expiry_date: str | None
	product_id: int

	@staticmethod
	def from_db(supply: Supply):
		return SupplyRead(
			id=supply.id,
			type=supply.type,
			unit_measure=supply.unit_measure,
			unit_quantity=supply.unit_quantity,
			expiry_date=supply.expiry_date.isoformat() if supply.expiry_date else None,
			product_id=supply.product_id
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
		supply = self.model_dump(exclude_none=True)
		return {
			**supply,
			"type": supply_type,
		}

class SupplyUpdate(SupplyBase):
	unit_measure: str | None
	unit_quantity: int | None
	type_id: int | None
	expiry_date: str | None
	
	def update_dump(self):
		if self.unit_measure == "":
			self.unit_measure = None
		if self.unit_quantity == "":
			self.unit_quantity = None
   
		if (self.expiry_date != None 
      and self.expiry_date != ""):
			self.expiry_date = datetime.strptime(self.expiry_date, "%d/%m/%Y").isoformat()
   
		supply_type = None
		if self.type_id != None:
			if (isinstance(self.type_id, int)
       and 0 > self.type_id > len(TYPE_SUPPLY_BY_ID)):
				supply_type = TypeSupply(TYPE_SUPPLY_BY_ID.get(self.type_id)).value
		supply = self.model_dump(exclude_none=True)
		if supply_type != None:
			supply["type"] = supply_type
		return supply

