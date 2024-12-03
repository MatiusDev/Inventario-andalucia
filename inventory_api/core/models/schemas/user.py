from typing import Any
from sqlmodel import Field, SQLModel

from models.entities.user import User
from models.enums.role import Role as ROLES

# Un usuario DTO nuevo para BD o para registro en Auth
class UserCreate(SQLModel):
  username: str
  password: str
  full_name: str
  email: str

# Un usuario DTO ya existente en BD
class UserRead(SQLModel):
  id: Any | None
  username: str
  full_name: str
  email: str
  role: str
  active: bool
  created_at: str
  updated_at: str
  last_session: str
  
  @staticmethod
  def from_user(user: User):
    return UserRead(
      id = user.id,
      username = user.username,
      full_name = user.full_name,
      email = user.email,
      role = ROLES(user.role_id).name if user.role_id else None,
      active = user.active,
      created_at = user.created_at.isoformat(),
      updated_at = user.updated_at.isoformat(),
      last_session = user.last_session.isoformat()
    )

# Usuario para login desde Front
class UserAuth(SQLModel):
  username: str
  password: str

# Usuario con Token para guardar la sesión
class UserToken(SQLModel):
  id: Any
  username: str
  full_name: str
  email: str
  role: str
  active: bool
  created_at: str
  updated_at: str
  last_session: str
  token: str | None = Field(None)