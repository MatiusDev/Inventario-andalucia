from fastapi import APIRouter

from models.schemas.role import RoleCreate

from services.role_service import SRoleDependency

route = APIRouter()

@route.get("/")
def get_all_roles(role_service: SRoleDependency):
  return role_service.get_all()

@route.get("/{id}")
def get_role(id: int, role_service: SRoleDependency):
  return role_service.get_by_id(id)
  
@route.post("/")
def create_role(role: RoleCreate, role_service: SRoleDependency):
  return role_service.create(role)

@route.put("/{id}")
def update_role(id: int, role: RoleCreate, role_service: SRoleDependency):
  return role_service.update(id, role)

@route.delete("/{id}")
def delete_role(id: int, role_service: SRoleDependency):
  return role_service.delete(id)