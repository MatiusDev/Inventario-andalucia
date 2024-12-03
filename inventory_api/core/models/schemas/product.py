from datetime import date
from enum import Enum
from typing import Any
from sqlmodel import Field, SQLModel


class typeProduct_Enum(str, Enum):
  PLANT = "Plantas"
  SUPPLY = "Insumos"
  TOOL = "Herramientas"

class state_Enum(str, Enum):
  AVAILABLE = "Disponible"
  PENDING = "Pendiente"
  SPENT = "Agotado"

class ProductBase(SQLModel):
  name: str = Field(default=None)
  price: float = Field(default=None)
  stock: int = Field(default=None)
  stock_minimum: int = Field(default=None)
  location: str = Field(default=None)
  date_entry: date = Field(default=None)
  date_upate: date = Field(default=None)
  state: state_Enum = Field(default=state_Enum.AVAILABLE)
  type_product: typeProduct_Enum = Field(default="---Selecciona un tipo---")

# Esquemas de validación in/out de datos de producto
# class ProductCreate(SQLModel):
#   name: str
#   price: float
  
class ProductCreate(ProductBase):
  pass
  

class ProductRead(SQLModel):
  id: Any | None
  name: str
  price: float
  