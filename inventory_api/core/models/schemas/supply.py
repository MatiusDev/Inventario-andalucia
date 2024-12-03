from datetime import date
from enum import Enum
from pydantic import validator
from sqlmodel import SQLModel, Field

class TypeInput_Enum(str, Enum): 
    SEMILLAS = "Semillas",
    FERTILIZANTES = "Fertilizantes",
    PESTICIDAS = "Pesticidas",
    HERBICIDAS = "Herbicidas",
    SUSTRATOS = "Sustratos"

class SupplyBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    id_product: int = Field(foreign_key="product.id")
    type_input: TypeInput_Enum = Field(default=TypeInput_Enum.SEMILLAS)
    expiration_date: date = Field(default=None)
    unit_measure: str = Field(default=None)
    supplier: str = Field(default=None)

    @validator("expiration_date")
    def validate_expiration_date(cls, value):
        if value < date.today():
            raise ValueError("La fecha de expiración no puede ser anterior a la fecha actual.")
        return value
    
class SupplyCreate(SupplyBase):
    pass

class SupplyUpdate(SupplyBase):
    pass