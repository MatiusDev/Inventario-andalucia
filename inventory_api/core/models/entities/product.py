from sqlmodel import Field, SQLModel
# Entidad DB Producto
class Product(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  name: str
  price: float