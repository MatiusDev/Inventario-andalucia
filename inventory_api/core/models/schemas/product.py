from datetime import date
from enum import Enum
from typing import Any
from sqlmodel import SQLModel


class typeProduct_Enum(str, Enum):
  PLANT = "Plantas"
  SUPPLY = "Insumos"
  TOOL = "Herramientas"

class state_Enum(str, Enum):
  AVAILABLE = "Disponible"
  PENDING = "Pendiente"
  SPENT = "Agotado"

class ProductBase(SQLModel):
  name: str
  price: float
  # stock: int
  # stock_minimum: int
  # location: str
  # date_entry: date
  # date_upate: date
  # state: str
  # type_product: str

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
  