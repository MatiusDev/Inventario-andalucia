from typing import Annotated
from fastapi import Depends, Request

from config.db_adapter import DBSession
from config.auth_token import AuthDependency

from sqlmodel import select

from models.entities.role import Role
from models.schemas.role import RoleCreate, RoleRead
from models.enums.role import RoleType, Permissions

class RoleService:
  def __init__(self, db: DBSession, auth: AuthDependency, request: Request) -> None:
    self.db = db
    self.auth = auth
    self.request = request
  
  async def get_all(self):
    try:
      user = await self.auth.get_user(self.request)
      
      if (user.role == RoleType.USER
          or Permissions.READ not in user.permissions):
        return { "status_code": 403, "detail": "No tienes permisos para acceder a este recurso", "status": "fail" }
                 
      roles = self.db.exec(select(Role)).all() or []
      return { "data" : roles, "status": "success" }
    except Exception as err:
      return { "status_code": 500, "detail": str(err), "status": "error"}
  
  async def get_by_id(self, id: int):
    user = await self.auth.get_user(self.request)
    
    if (user.role == RoleType.USER
        or Permissions.READ not in user.permissions):
      return { "status_code": 403, "detail": "No tienes permisos para acceder a este recurso", "status": "fail" }
      
    role = self.db.get(Role, id)
    
    if role == None:
      return { "status_code": 404, "detail": "Rol no encontrado", "status": "fail" }
    
    read_role = RoleRead.model_validate(role)
    return { "data": read_role, "status": "success" }

  async def create(self, role: RoleCreate):
    try:
      user = await self.auth.get_user(self.request)
      
      if (user.role == RoleType.USER
          or Permissions.EDIT not in user.permissions):
        return { "status_code": 403, "detail": "No tienes permisos para acceder a este recurso", "status": "fail" }
      
      new_role = Role.model_validate(role)
      self.db.add(new_role)
      self.db.commit()
      self.db.refresh(new_role)
      
      read_role = RoleRead.model_validate(new_role)
      return { "data": read_role, "status": "success" }
    except Exception as err:
      return { "status_code": 500, "detail": str(err), "status": "error" }

  async def update(self, id: int, role: RoleCreate):
    try:
      user = await self.auth.get_user(self.request)
      
      if (user.role == RoleType.USER
          or Permissions.EDIT not in user.permissions):
        return { "status_code": 403, "detail": "No tienes permisos para acceder a este recurso", "status": "fail" }
      
      role_db = self.db.get(Role, id)

      if role_db == None:
        return { "status_code": 404, "detail": "Rol no encontrado", "status": "fail" }
      
      role_db.name = role.name
      role_db.description = role.description
      role_db.permissions = role.permissions
      self.db.add(role_db)
      self.db.commit()
      self.db.refresh(role_db)
      
      read_role = RoleRead.model_validate(role_db)
      return { "data": read_role, "status": "success" }
    except Exception as err:
      return {  "status_code": 500, "detail": str(err), "status": "error" }

  async def delete(self, id: int):
    try:
      user = await self.auth.get_user(self.request)
      
      if (user.role == RoleType.USER
          or Permissions.DELETE not in user.permissions):
        return { "status_code": 403, "detail": "No tienes permisos para acceder a este recurso", "status": "fail" }
      
      role = self.db.get(Role, id)
      
      if role == None:
        return { "status_code": 404, "detail": "Rol no encontrado", "status": "fail" }
      
      self.db.delete(role)
      self.db.commit()
      return { "message": "Rol eliminado", "status": "success" }
    except Exception as err:
      return { "status_code": 500, "detail": str(err), "status": "error" }
  
SRoleDependency = Annotated[RoleService, Depends(RoleService)]
    