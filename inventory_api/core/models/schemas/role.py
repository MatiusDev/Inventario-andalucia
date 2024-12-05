from typing import Any
from sqlmodel import SQLModel
# Esquemas de validación in/out de datos de rol
class RoleCreate(SQLModel):
  name: str
  description: str
  permissions: str

class RoleRead(SQLModel):
  id: Any | None
  name: str
  description: str
  permissions: str
  