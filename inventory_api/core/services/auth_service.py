from typing import Annotated
from fastapi import Depends

from fastapi_auth_jwt.backend import JWTHandler, jwt

import bcrypt
# Modelos y Esquemas
from models.schemas.user import UserCreate, UserAuth, UserToken 
# Dependencias
from config.auth_token import AuthDependency
from services.user_service import SUserDependency

class AuthService:
  def __init__(self, auth: AuthDependency, user: SUserDependency) -> None:
    self.auth = auth
    self.user = user
  
  async def sign_up(self, user: UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())
    user.password = hashed_password.decode("utf-8")
    user_info = await self.user.create(user)

    if user_info["status"] != "success":
      return user_info
       
    return { "message": "Usuario registrado correctamente", "status": "success" }
  
  async def login(self, user: UserAuth):
    
    
    user_data = self.user.get_by_username(user.username)
    
    if user_data["status"] != "success":
      print("HERE")
      return user_data
    
    user_info, user_password = user_data["data"]
    
    if not bcrypt.checkpw(user.password.encode("utf-8"), user_password.encode("utf-8")):
      return { "status_code": 401, "detail": "Credenciales invalidas", "status": "fail" }
    
    user_token = UserToken.model_validate(user_info)
    token = await self.auth.create_token(user_token)
    
    return { "token": token, "status": "success" }
  
  async def logout(self, token: str):
    await self.auth.invalidate_token(token)
    return { "message": "Sesión cerrada", "status": "success" }
    
SAuthDependency = Annotated[AuthService, Depends(AuthService)]