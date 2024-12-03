from typing import List
from fastapi import APIRouter

from models.schemas.role import RoleCreate, RoleRead

from services.role_service import SRoleDependency

from utils.response_handler import response_handler

route = APIRouter()

@route.get("/", status_code=200, response_model=List[RoleRead])
async def get_all_roles(role_service: SRoleDependency):
  return await response_handler(role_service.get_all())

@route.get("/{id}", status_code=200, response_model=RoleRead)
async def get_role(id: int, role_service: SRoleDependency):
  return role_service.get_by_id(id)
  
@route.post("/", status_code=201, response_model=RoleRead)
async def create_role(role: RoleCreate, role_service: SRoleDependency):
  return role_service.create(role)

@route.put("/{id}", status_code=200, response_model=RoleRead)
async def update_role(id: int, role: RoleCreate, role_service: SRoleDependency):
  return role_service.update(id, role)

@route.delete("/{id}", status_code=200)
async def delete_role(id: int, role_service: SRoleDependency):
  return role_service.delete(id)