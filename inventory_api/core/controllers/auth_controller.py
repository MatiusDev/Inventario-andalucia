from fastapi import APIRouter
from services.auth_service import SAuthDependency

from models.schemas.user import UserAuth, UserCreate

from utils.response_handler import response_handler

route = APIRouter()

@route.post("/sign-up", status_code=201)
async def sign_up(user: UserCreate, auth_service: SAuthDependency):
  return await response_handler(auth_service.sign_up(user))

@route.post("/login", status_code=200)
async def login(user: UserAuth, auth_service: SAuthDependency):
  return await response_handler(auth_service.login(user))

# Pendiente por modificar
@route.post("/logout", status_code=200)
async def logout(auth_service: SAuthDependency):
  return await response_handler(auth_service.logout())