from sqlmodel import SQLModel, Field, Relationship

from models.entities.product import Product

class Tool(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    id_product: int = Field(foreign_key="product.id")
    category: str = Field(default="Manual")
    material: str = Field(default=None)
    brand: str = Field(default=None)
    type_maintenance: str = Field(default="Limpieza")
    product_data: Product = Relationship(back_populates="tools")