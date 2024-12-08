from sqlmodel import SQLModel, Field

class OrderSupplier(SQLModel, table=True):
  id_order: int = Field(default=None, primary_key=True, foreign_key="order.id")
  id_supplier: int = Field(default=None, primary_key=True, foreign_key="supplier.id")