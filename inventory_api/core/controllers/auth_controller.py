from fastapi import APIRouter
from services.auth_service import SAuthDependency

from models.schemas.user import LoginUser

from config.auth_token import auth_backend

route = APIRouter()

@route.post("/sign-up")
async def sign_up(user: LoginUser, user_service: SAuthDependency):
  print(user)

# @route.post("/login")
# async def login(user: LoginUser, user_service: SAuthDependency):
#   return await user_service.login(user)

@route.post("/login")
async def login(user: LoginUser):
  token = await auth_backend.create_token(
      {
        "username": user.username,
        "password": user.password
      }
    )
  return { "token": token }


@route.get("/profile-info")
async def get_profile_info():
  pass

@route.post("logout")
async def logout(user_service: SAuthDependency):
  pass