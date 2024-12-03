from typing import Annotated
from fastapi import Depends, HTTPException, Request

from config.db_adapter import DBSession
from config.auth_token import AuthDependency

from sqlmodel import select

from models.entities.role import Role
from models.schemas.role import RoleCreate, RoleRead
from models.enums.role import Role as ROLES


class RoleService:
  def __init__(self, db: DBSession, auth: AuthDependency, request: Request) -> None:
    self.db = db
    self.auth = auth
    self.request = request
  
  async def get_all(self):
    try:
      user = await self.auth.get_user(self.request)
      
      if user.role == ROLES.USER.name:
        return { "status_code": 401, "detail": "No tienes permisos para acceder a este recurso", "status": "fail" }
                 
      roles = self.db.exec(select(Role)).all() or []
      return { "data" : roles, "status": "success" }
    except Exception as err:
      return { "status_code": 500, "detail": str(err), "status": "error"}
  
  async def get_by_id(self, id: int):
    role = self.db.get(Role, id)
    user = await self.auth.get_user(self.request)
    
    if user.role == ROLES.USER.name:
        return { "status_code": 401, "detail": "No tienes permisos para acceder a este recurso", "status": "fail" }
    
    if role == None:
      return { "status_code": 404, "detail": "Rol no encontrado", "status": "fail" }
    
    read_role = RoleRead.model_validate(role.model_dump())
    return { "data": read_role, "status": "success" }

  def create(self, role: RoleCreate):
    new_role = Role(
      name=role.name,
      permissions=role.permissions,
      description=role.description
    )
    self.db.add(new_role)
    self.db.commit()
    self.db.refresh(new_role)
    
    read_role = RoleRead(
      id=new_role.id,
      name=new_role.name,
      permissions=new_role.permissions,
      description=new_role.description
    )
    
    return read_role

  def update(self, id: int, role: RoleCreate):
    role_db = self.db.get(Role, id)

    if role_db == None:
      raise HTTPException(status_code=404, detail="Rol no encontrado")
    
    role_db.name = role.name
    role_db.description = role.description
    role_db.permissions = role.permissions
    self.db.add(role_db)
    self.db.commit()
    self.db.refresh(role_db)
    
    read_role = RoleRead.model_validate(role_db.model_dump())
    
    return read_role

  def delete(self, id: int):
    role = self.db.get(Role, id)
    
    if role == None:
      raise HTTPException(status_code=404, detail="Rol no encontrado")
    
    self.db.delete(role)
    self.db.commit()
    return {"message": "Rol eliminado", "status": "success"}
  
SRoleDependency = Annotated[RoleService, Depends(RoleService)]
    