from sqlmodel import SQLModel, Field, Relationship

from models.entities.product import Product

class Plant(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    id_product: int = Field(foreign_key="product.id")
    name_scientific: str = Field(default=None)
    type_plant: str = Field(default="exterior")
    required_watering: str = Field(default="diario")
    required_light: str = Field(default="sombra")
    ideal_temperature: int = Field(default=None)
    life_time: str = Field(default="Si")
    product_data: Product = Relationship(back_populates="plants")
