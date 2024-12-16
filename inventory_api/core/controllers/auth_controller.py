from fastapi import APIRouter
from core.services.auth_service import SAuthDependency

from core.models.schemas.user import UserAuth, UserCreate

from core.utils.response_handler import response_handler

route = APIRouter()

@route.get("/profile", status_code=200)
async def profile(auth_service: SAuthDependency):
  return await response_handler(auth_service.profile())

@route.post("/sign-up", status_code=201)
async def sign_up(user: UserCreate, auth_service: SAuthDependency):
  return await response_handler(auth_service.sign_up(user))

@route.post("/login", status_code=200)
async def login(user: UserAuth, auth_service: SAuthDependency):
  return await response_handler(auth_service.login(user))

@route.post("/logout", status_code=200)
async def logout(auth_service: SAuthDependency):
  return await response_handler(auth_service.logout())