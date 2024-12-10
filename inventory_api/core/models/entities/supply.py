from datetime import datetime
from sqlalchemy import TIMESTAMP, Column, text
from sqlmodel import SQLModel, Field, Relationship

class Supply(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    type: str
    unit_measure: str
    unit_quantity: int
    expiry_date: datetime | None = Field(sa_column=Column(
      TIMESTAMP(timezone=True),
      nullable=False,
      server_default=text("CURRENT_TIMESTAMP"),
      default=text("CURRENT_TIMESTAMP")
    ), default=None)
    
    product_id: int | None = Field(default=None, unique=True, foreign_key="product.id")
    products: list["Product"] = Relationship(back_populates="supply") # type: ignore
