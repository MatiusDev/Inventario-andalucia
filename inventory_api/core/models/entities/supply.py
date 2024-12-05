from datetime import datetime
from sqlalchemy import TIMESTAMP, Column, text
from sqlmodel import SQLModel, Field, Relationship

class Supply(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    type: str = Field(default="Semillas")
    unit_measure: str | None = Field(default=None)
    supplier: str | None = Field(default=None)
    expiration_date: datetime | None = Field(default=None)
    
    id_product: int = Field(foreign_key="product.id")
    products: list["Product"] = Relationship(back_populates="supply") # type: ignore
