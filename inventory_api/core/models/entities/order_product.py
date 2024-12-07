from sqlmodel import SQLModel, Field

class OrderProduct(SQLModel, table=True):
  id_order: int = Field(default=None, primary_key=True, foreign_key="order.id")
  id_product: int = Field(default=None, primary_key=True, foreign_key="product.id")