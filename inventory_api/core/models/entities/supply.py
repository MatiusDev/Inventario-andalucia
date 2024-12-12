from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

class Supply(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    type: str
    unit_measure: str
    unit_quantity: int
    expiry_date: datetime | None = Field(default=None, nullable=True)
    product_id: int | None = Field(default=None, unique=True, foreign_key="product.id")
    
    products: list["Product"] = Relationship(back_populates="supply") # type: ignore
