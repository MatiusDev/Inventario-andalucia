from typing import Any
from sqlmodel import SQLModel
# Esquemas de validación in/out de datos de producto
class ProductCreate(SQLModel):
  name: str
  price: float

class ProductRead(SQLModel):
  id: Any | None
  name: str
  price: float
  
class ProductBase(SQLModel):
  id: int
  quantity: int
  