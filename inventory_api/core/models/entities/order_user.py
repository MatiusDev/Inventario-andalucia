from sqlmodel import SQLModel, Field

class OrderUser(SQLModel, table=True):
  id_order: int = Field(default=None, primary_key=True, foreign_key="order.id")
  id_user: int = Field(default=None, primary_key=True, foreign_key="user.id")