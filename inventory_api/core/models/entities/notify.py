from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship, Column, text, TIMESTAMP


class Notify(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  message: str
  date_notification: datetime | None = Field(sa_column=Column(
    TIMESTAMP(timezone=True),
    nullable=False,
    server_default=text("CURRENT_TIMESTAMP"),
    default=text("CURRENT_TIMESTAMP")
  ))
  
  id_product: int = Field(foreign_key="product.id")

  products: list["Product"] = Relationship(back_populates="notify")