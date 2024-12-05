from datetime import datetime
from enum import Enum
# from pydantic import field_validator
from sqlmodel import SQLModel, Field

from models.entities.supply import Supply
from datetime import datetime

class TypeInput_Enum(str, Enum): 
    SEMILLAS = "Semillas",
    FERTILIZANTES = "Fertilizantes",
    PESTICIDAS = "Pesticidas",
    HERBICIDAS = "Herbicidas",
    SUSTRATOS = "Sustratos"

class SupplyBase(SQLModel):
    type: str
    
    unit_measure: str
    supplier: str

    # @field_validator("expiration_date")
    # def validate_expiration_date(cls, value):
    #     if value < date.today():
    #         raise ValueError("La fecha de expiración no puede ser anterior a la fecha actual.")
    #     return value
    
class SupplyRead(SupplyBase):
    id: int | None
    expiration_date: datetime | None
    
class SupplyCreate(SupplyBase):
    id_product: int
    expiration_date: str | None
    
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