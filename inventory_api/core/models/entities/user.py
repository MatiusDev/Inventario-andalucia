from sqlmodel import SQLModel, Field, TIMESTAMP, Column, text
from pydantic import field_validator
from datetime import datetime

from models.enums.role import Role as ROLES

class User(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  username: str = Field(unique=True)
  password: str
  full_name: str
  email: str = Field(unique=True)
  active: bool | None = Field(default=True)
  created_at: datetime | None = Field(sa_column=Column(
    TIMESTAMP(timezone=True),
    nullable=False,
    server_default=text("CURRENT_TIMESTAMP"),
    default=text("CURRENT_TIMESTAMP")
  ), default_factory=datetime.now)
  updated_at: datetime | None = Field(sa_column=Column(
    TIMESTAMP(timezone=True),
    nullable=False,
    server_default=text("CURRENT_TIMESTAMP"),
    default=text("CURRENT_TIMESTAMP")
  ), default_factory=datetime.now)
  last_session: datetime | None = Field(sa_column=Column(
    TIMESTAMP(timezone=True),
    nullable=False,
    server_default=text("CURRENT_TIMESTAMP"),
    default=text("CURRENT_TIMESTAMP")
  ), default_factory=datetime.now)
  
  role_id: int | None = Field(default=ROLES.USER.value, foreign_key="role.id")