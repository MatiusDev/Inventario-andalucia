from sqlmodel import SQLModel, Field, Relationship

class Role(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  name: str
  description: str
  permissions: str
  users: list["User"] = Relationship(back_populates="role") # type: ignore