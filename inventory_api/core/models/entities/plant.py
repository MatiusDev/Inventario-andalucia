from sqlmodel import SQLModel, Field, Relationship
from ..enums.plant import Plant_type_Enum, Irrigation_Enum, Light_Enum

from models.entities.product import Product

class Plant(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    scientific_name: str
    type_plant: Plant_type_Enum = Field(default=Plant_type_Enum.ORNAMENTAL)
    required_irrigation: Irrigation_Enum
    required_light: Light_Enum
    ideal_temperature: int
    perishable: bool = Field(default=True)
    
    
    id_product: int = Field(foreign_key="product.id")
    products: list["Product"] = Relationship(back_populates="plant")
