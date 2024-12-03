from datetime import date
from sqlmodel import SQLModel, Field, Relationship

from models.entities.product import Product

class Supply(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    id_product: int = Field(foreign_key="product.id")
    type_input: str = Field(default="Semillas")
    expiration_date: date = Field(default=None)
    unit_measure: str = Field(default=None)
    supplier: str = Field(default=None)
    product_data: Product = Relationship(back_populates="supplies")
