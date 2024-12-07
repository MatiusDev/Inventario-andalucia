from fastapi import APIRouter

from models.schemas.role import RoleCreate

from services.role_service import SRoleDependency

from utils.response_handler import response_handler

route = APIRouter()

@route.get("/", status_code=200)
async def get_all(role_service: SRoleDependency):
  return await response_handler(role_service.get_all())

@route.get("/{id}", status_code=200)
async def get_by_id(id: int, role_service: SRoleDependency):
  return await response_handler(role_service.get(id))
  
@route.post("/", status_code=201)
async def create_role(role: RoleCreate, role_service: SRoleDependency):
  return await response_handler(role_service.create(role))

@route.put("/{id}", status_code=200)
async def update_role(id: int, role: RoleCreate, role_service: SRoleDependency):
  return await response_handler(role_service.update(id, role))

@route.delete("/{id}", status_code=200)
async def delete_role(id: int, role_service: SRoleDependency):
  return await response_handler(role_service.delete(id))
