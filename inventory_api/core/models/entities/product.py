from sqlmodel import Field, SQLModel, Relationship

from models.entities.order_product import OrderProduct

# Entidad DB Producto
class Product(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  name: str
  price: float
  
  orders: list["Order"] = Relationship(back_populates="products", link_model=OrderProduct) # type: ignore
  

  