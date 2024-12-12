from sqlmodel import SQLModel, Field, Relationship

from core.models.entities.product import Product

class Tool(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    category: str 
    material: str
    brand: str
    type_maintenance: str | None = Field(default=None)
    
    id_product: int = Field(foreign_key="product.id")