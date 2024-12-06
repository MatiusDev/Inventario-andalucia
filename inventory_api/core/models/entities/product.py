# from datetime import date
from sqlmodel import Field, SQLModel, Relationship


# Entidad DB Producto
class Product(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  name: str
  price: float
  # stock: int
  # stock_minimum: int
  # location: str
  # date_entry: date
  # date_upate: date
  # state: str
  # type_product: str
  
  supply: "Supply" = Relationship(back_populates="products") # type: ignore
  plant: "Plant" = Relationship(back_populates="products")
  
  