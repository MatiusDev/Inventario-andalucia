from datetime import date, datetime
from sqlmodel import Field, SQLModel, Relationship, TIMESTAMP, Column, text
# Entidad DB Producto
class Product(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  name: str
  price: float
  description: str
  stock: int
  stock_minimum: int
  location: str
  date_entry: datetime | None = Field(sa_column=Column(
    TIMESTAMP(timezone=True),
    nullable=False,
    server_default=text("CURRENT_TIMESTAMP"),
    default=text("CURRENT_TIMESTAMP")
  ), default_factory=datetime.now)
  date_update: datetime | None = Field(sa_column=Column(
    TIMESTAMP(timezone=True),
    nullable=False,
    server_default=text("CURRENT_TIMESTAMP"),
    default=text("CURRENT_TIMESTAMP")
  ), default_factory=datetime.now)
  state: str
  # type_product: str
  
  supply: "Supply" = Relationship(back_populates="products") # type: ignore
  
  