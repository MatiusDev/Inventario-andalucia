from sqlmodel import Field, SQLModel, Relationship, TIMESTAMP, Column, text
from datetime import datetime

# Entidad DB Producto
class Product(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  name: str
  price: float
  description: str
  stock: int 
  stock_minimum: int
  location: str | None = Field(default=None)
  active: bool | None = Field(default=True)
  type: str
  created_at: datetime | None = Field(sa_column=Column(
    TIMESTAMP(timezone=True),
    nullable=False,
    server_default=text("CURRENT_TIMESTAMP"),
    default=text("CURRENT_TIMESTAMP")
  ), default_factory=datetime.now)
  updated_at: datetime | None = Field(sa_column=Column(
    TIMESTAMP(timezone=True),
    nullable=False,
    server_default=text("CURRENT_TIMESTAMP"),
    default=text("CURRENT_TIMESTAMP")
  ), default_factory=datetime.now)
  
  supply: "Supply" = Relationship(back_populates="products") # type: ignore
  orders: list["OrderProduct"] = Relationship(back_populates="product") # type: ignore
  plant: "Plant" = Relationship(back_populates="products") # type: ignore
  tool: "Tool" = Relationship(back_populates="products") # type: ignore
  