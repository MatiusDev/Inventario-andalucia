from fastapi import APIRouter

from models.schemas.user import UserCreate

from services.user_service import SUserDependency

from utils.response_handler import response_handler

route = APIRouter()

@route.get("/", status_code=200)
async def get_all_users(user_service: SUserDependency):
  return await response_handler(user_service.get_all())

@route.get("/{id}", status_code=200)
async def get_user(id: int, user_service: SUserDependency):
  return await response_handler(user_service.get_by_id(id))
  
@route.post("/", status_code=201)
async def create_user(user: UserCreate, user_service: SUserDependency):
  return await response_handler(user_service.create(user))

@route.put("/{id}", status_code=200)
async def update_user(id: int, user: UserCreate, user_service: SUserDependency):
  return await response_handler(user_service.update(id, user))

@route.delete("/{id}", status_code=200)
async def delete_user(id: int, user_service: SUserDependency):
  return await response_handler(user_service.delete(id))