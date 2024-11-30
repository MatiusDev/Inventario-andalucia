from typing import Any
from sqlmodel import Field, SQLModel

# Un usuario DTO nuevo para BD
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
  
class UserAuthRead(UserRead):
  password: str

# Usuario para login desde Front
class UserAuth(SQLModel):
  username: str
  password: str

# Usuario para un registro desde Front
class UserRegister(SQLModel):
  username: str
  password: str
  full_name: str
  email: str

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