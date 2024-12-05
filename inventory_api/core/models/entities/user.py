from sqlmodel import SQLModel, Field, TIMESTAMP, Column, text, UniqueConstraint, Relationship
from datetime import datetime

from models.enums.role import RoleID

class User(SQLModel, table=True):
  __table_args__ = (
    UniqueConstraint("username", name="unique_username"),
    UniqueConstraint("email", name="unique_email"),
  )
  
  id: int | None = Field(default=None, primary_key=True)
  username: str = Field(unique=True)
  password: str
  full_name: str
  email: str = Field(unique=True)
  active: bool = Field(default=True)
  is_logged_in: bool = Field(default=False)
  login_attempts: int = Field(default=0)
  created_at: datetime = Field(sa_column=Column(
    TIMESTAMP(timezone=True),
    nullable=False,
    server_default=text("CURRENT_TIMESTAMP"),
    default=text("CURRENT_TIMESTAMP")
  ), default_factory=datetime.now)
  updated_at: datetime = Field(sa_column=Column(
    TIMESTAMP(timezone=True),
    nullable=False,
    server_default=text("CURRENT_TIMESTAMP"),
    default=text("CURRENT_TIMESTAMP")
  ), default_factory=datetime.now)
  last_session: datetime = Field(sa_column=Column(
    TIMESTAMP(timezone=True),
    nullable=False,
    server_default=text("CURRENT_TIMESTAMP"),
    default=text("CURRENT_TIMESTAMP")
  ), default_factory=datetime.now)
  
  role_id: int = Field(default=RoleID.USER.value, foreign_key="role.id")
  role: "Role" = Relationship(back_populates="users") # type: ignore