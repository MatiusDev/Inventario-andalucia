from datetime import date, datetime
from sqlalchemy import TIMESTAMP, Column, text
from sqlmodel import SQLModel, Field, Relationship

class Supply(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    type_supply: str
    unit_measure: str
    expiry_date: datetime
    
    id_product: int = Field(foreign_key="product.id")
    products: list["Product"] = Relationship(back_populates="supply") # type: ignore
