from fastapi import APIRouter
from services.auth_service import SAuthDependency

from models.schemas.user import UserAuth, UserRegister

route = APIRouter()

@route.post("/sign-up")
async def sign_up(user: UserRegister, auth_service: SAuthDependency):
  return await auth_service.sign_up(user)

@route.post("/login")
async def login(user: UserAuth, auth_service: SAuthDependency):
  return await auth_service.login(user)

# Pendiente por modificar
@route.post("/logout")
async def logout(user: UserAuth, auth_service: SAuthDependency):
  return await auth_service.logout(user)