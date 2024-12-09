from datetime import date, datetime
from enum import Enum
# from pydantic import field_validator
from sqlmodel import SQLModel, Field

from models.entities.supply import Supply
from models.enums.supplies import TypeSupply
from datetime import datetime

class SupplyBase(SQLModel):
    type_supply: str
    unit_measure: str
    expiry_date: date
    
class SupplyRead(SupplyBase):
    id: int | None
    type_supply: str
    unit_measure: str
    expiry_date: date
    
class SupplyCreate(SupplyBase):
    id_product: int
    
    @staticmethod
    def supply_dump(self):
        print(self.expiration_date)
        return {
            "id_product": self.id_product,
            "type": self.type,
            "expiration_date": datetime.strptime(self.expiration_date, "%d/%m/%Y"),
            "unit_measure": self.unit_measure,
            "supplier": self.supplier
        }
        

class SupplyUpdate(SupplyBase):
    pass