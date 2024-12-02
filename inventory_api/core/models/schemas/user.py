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
    # model_dump convierte todos los datos del usuarioDB a un diccionario
    user_dump = user.model_dump()
    # Se agrega el campo rol al diccionario
    user_dump["role"] = ROLES(user.role_id).name if user.role_id else None
    # Se elimina el campo role_id del diccionario
    user_dump.pop("role_id", None)
    # Se retorna el usuario validado con los campos que necesita el esquema
    return UserRead.model_validate(user_dump)

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