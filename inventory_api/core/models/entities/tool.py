from sqlmodel import SQLModel, Field, Relationship

from models.entities.product import Product
from models.schemas.tool import CategoryEnum, TypeMaintenance_Enum, MaterialEnum

class Tool(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    category: str = Field(default=CategoryEnum.APERO)
    material: str = Field(default=MaterialEnum.MADERA)
    brand: str
    type_maintenance: str | None = Field(default=TypeMaintenance_Enum.CORRECTIVO)
    # product_data: Product = Relationship(back_populates="tools")
    
    id_product: int = Field(foreign_key="product.id")