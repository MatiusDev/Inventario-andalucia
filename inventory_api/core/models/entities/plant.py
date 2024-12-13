from sqlmodel import SQLModel, Field, Relationship


class Plant(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    scientific_name: str
    type: str
    required_irrigation: str
    required_light: str
    ideal_temperature: int
    product_id: int | None = Field(default=None, unique=True, foreign_key="product.id")
         
    products: list["Product"] = Relationship(back_populates="plant") # type: ignore
