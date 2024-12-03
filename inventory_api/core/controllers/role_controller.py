from fastapi import APIRouter

from models.schemas.role import RoleCreate

from services.role_service import SRoleDependency

from utils.response_handler import response_handler

route = APIRouter()

@route.get("/", status_code=200)
async def get_all_roles(role_service: SRoleDependency):
  return await response_handler(role_service.get_all())

@route.get("/{id}")
async def get_role(id: int, role_service: SRoleDependency):
  return role_service.get_by_id(id)
  
@route.post("/")
async def create_role(role: RoleCreate, role_service: SRoleDependency):
  return role_service.create(role)

@route.put("/{id}")
async def update_role(id: int, role: RoleCreate, role_service: SRoleDependency):
  return role_service.update(id, role)

@route.delete("/{id}")
async def delete_role(id: int, role_service: SRoleDependency):
  return role_service.delete(id)