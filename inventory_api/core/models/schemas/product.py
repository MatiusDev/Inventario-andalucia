from datetime import date, datetime
from enum import Enum
from typing import Any
from sqlmodel import Field, SQLModel

from models.enums.type_Product import Type_Product
from models.entities.product import Product
from models.entities.supply import Supply

class ProductBase(SQLModel):
  name: str
  price: float
  description: str
  stock: int
  stock_minimum: int
  location: str
  state: str
  type_product: str

class ProductCreate(ProductBase):
  pass

class ProductUpdate(ProductBase):
  pass
  
class ProductRead(SQLModel):
  id: Any | None
  name: str
  price: float
  description: str
  stock: int
  stock_minimum: int
  location: str
  state: str
  type_product: str
  
  @staticmethod
  def supply_and_product(product: Product, supply: Supply):
    return {
      "id": product.id,
      "Name": product.name,
      "Type": supply.type,
      "Price": product.price,
      "Unit_meausure": supply.unit_measure,
      "Supplier": supply.supplier,
      "Expiration_date": supply.expiration_date,
    }
  
class ProductBase(SQLModel):
  id: int
  quantity: int
  