from sqlmodel import Field, SQLModel, Relationship

# Entidad DB Producto
class Product(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  name: str
  price: float
  
  orders: list["OrderProduct"] = Relationship(back_populates="product") # type: ignore
  

  