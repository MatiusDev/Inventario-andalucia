from typing import Annotated
from fastapi import Depends, HTTPException

from config.db_adapter import DBSession

from sqlmodel import select

from models.entities.role import Role
from models.schemas.role import RoleCreate, RoleRead

class RoleService:
  def __init__(self, db: DBSession) -> None:
    self.db = db
  
  def get_all(self):
    roles = self.db.exec(select(Role)).all() or []
    return roles
  
  def get_by_id(self, id: int):
    role = self.db.get(Role, id)
    
    if role == None:
      raise HTTPException(status_code=404, detail="Rol no encontrado")
    
    read_role = RoleRead(
      id=role.id,
      name=role.name,
      permissions=role.permissions,
      description=role.description
    )
    
    return read_role

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
    role_db.price = role.price
    self.db.add(role_db)
    self.db.commit()
    self.db.refresh(role_db)
    
    read_role = RoleRead(
      id=role_db.id,
      name=role_db.name,
      permissions=role_db.permissions,
      description=role_db.description
    )
    
    return read_role

  def delete(self, id: int):
    role = self.db.get(Role, id)
    
    if role == None:
      raise HTTPException(status_code=404, detail="Rol no encontrado")
    
    self.db.delete(role)
    self.db.commit()
    return {"message": "Rol eliminado", "status": "success"}
  
SRoleDependency = Annotated[RoleService, Depends(RoleService)]
    