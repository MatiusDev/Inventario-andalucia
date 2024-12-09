from sqlmodel import SQLModel, Field, Relationship

class OrderProduct(SQLModel, table=True):
  id_order: int = Field(default=None, primary_key=True, foreign_key="order.id")
  id_product: int = Field(default=None, primary_key=True, foreign_key="product.id")
  quantity: int
  
  order: "Order" = Relationship(back_populates="products") # type: ignore
  product: "Product" = Relationship(back_populates="orders") # type: ignore
