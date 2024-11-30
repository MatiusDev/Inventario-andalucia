from sqlmodel import SQLModel, Field, TIMESTAMP, Column, text
from datetime import datetime

class User(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  username: str = Field(unique=True)
  password: str
  full_name: str
  email: str = Field(unique=True)
  active: bool = Field(default=True)
  created_at: datetime | None = Field(sa_column=Column(
    TIMESTAMP(timezone=True),
    nullable=False,
    server_default=text("CURRENT_TIMESTAMP"),
    default=text("CURRENT_TIMESTAMP")
  ))
  updated_at: datetime | None = Field(sa_column=Column(
    TIMESTAMP(timezone=True),
    nullable=False,
    server_default=text("CURRENT_TIMESTAMP"),
    default=text("CURRENT_TIMESTAMP")
  ))
  last_session: datetime | None = Field(sa_column=Column(
    TIMESTAMP(timezone=True),
    nullable=False,
    server_default=text("CURRENT_TIMESTAMP"),
    default=text("CURRENT_TIMESTAMP")
  ))
  
  role_id: int | None = Field(default=None, foreign_key="role.id")