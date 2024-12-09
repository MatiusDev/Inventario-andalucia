from datetime import date, datetime
from enum import Enum
from typing import Any
from sqlmodel import Field, SQLModel

from models.enums.type_Product import TYPE_PRODUCT_BY_ID, Type_Product
from models.entities.product import Product
from models.entities.supply import Supply

class ProductCreate(SQLModel):
  name: str
  price: float
  description: str
  stock: int
  stock_minimum: int
  location: str
  type_id: int
  def create_dump(self):
    product = self.model_dump(exclude_none=True)
    if product.get("type_product") is None:
      product["type_product"] = TYPE_PRODUCT_BY_ID.get(self.type_id)
      product.pop("type_id")
    return product

class ProductUpdate(SQLModel):
  name: str
  price: float
  description: str
  stock: int
  stock_minimum: int
  location: str
  state: bool
  type_product: str
  
class ProductRead(SQLModel):
  id: Any | None
  name: str
  price: float
  description: str
  stock: int
  stock_minimum: int
  location: str
  state: bool
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
  