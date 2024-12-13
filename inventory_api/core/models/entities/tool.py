from sqlmodel import SQLModel, Field, Relationship

from core.models.entities.product import Product

class Tool(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    category: str 
    brand: str
    type_maintenance: str | None = Field(default=None)
    product_id: int | None = Field(default=None, unique=True, foreign_key="product.id")

    products: list["Product"] = Relationship(back_populates="tool") # type: ignore



