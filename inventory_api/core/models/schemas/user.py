from typing import Tuple
from sqlmodel import Field, SQLModel

from models.entities.user import User

# Un usuario DTO nuevo para BD o para registro en Auth
class UserCreate(SQLModel):
  username: str
  password: str
  full_name: str
  email: str
  
class UserUpdate(SQLModel):
  full_name: str | None
  email: str | None
  password: str | None
  # role: str | None
  active: bool | None
  updated_at: str | None
  last_session: str | None

# Un usuario DTO ya existente en BD
class UserRead(SQLModel):
  id: int
  username: str
  full_name: str
  email: str
  role: str
  permissions: tuple
  active: bool
  is_logged_in: bool
  created_at: str
  updated_at: str
  last_session: str
  
  @staticmethod
  def from_user(user: User):
    def get_permissions(permissions: str):
      return tuple(permissions.split(" "))
   
    return UserRead(
      id = user.id,
      username = user.username,
      full_name = user.full_name,
      email = user.email,
      role = user.role.type,
      permissions = get_permissions(user.role.permissions),
      active = user.active,
      is_logged_in = user.is_logged_in,
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
  id: int
  username: str
  full_name: str
  email: str
  role: str
  permissions: tuple
  active: bool
  is_logged_in: bool
  created_at: str
  updated_at: str
  last_session: str
  token: str | None = Field(None)