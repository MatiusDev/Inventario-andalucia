from sqlmodel import SQLModel, Field

class User(SQLModel):
  username: str
  password: str
  token: str = Field(None)