from typing import Annotated
from fastapi import Depends, Request
from datetime import datetime, timedelta

import bcrypt
# Modelos y Esquemas
from core.models.schemas.user import UserCreate, UserAuth, UserToken, UserRead, UserUpdate
# Dependencias
from core.config.auth_token import AuthDependency, UserDependency
from core.services.user_service import SUserDependency

class AuthService:
  def __init__(self, auth: AuthDependency, user: UserDependency, user_service: SUserDependency, request: Request) -> None:
    self.auth = auth
    self.user = user
    self.user_service = user_service
    self.request = request
  
  async def sign_up(self, user: UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())
    user.password = hashed_password.decode("utf-8")
    user_info = self.user_service.create_user(user)

    if user_info["status"] != "success":
      return user_info
       
    return { "message": "Usuario registrado correctamente", "status": "success" }
  
  async def login(self, user: UserAuth):   
    user_data = self.user_service.get_session(username=user.username)
       
    if user_data["status"] != "success":
      return user_data
    
    user_session = user_data["data"]
    
    if (user_session.is_logged_in):
      logged_at = datetime.fromisoformat(user_session.last_session)
      elapsed_time = datetime.now() - logged_at
      
      if elapsed_time <= timedelta(seconds=20):
        return { "status_code": 400, "detail": "Ya estás logueado", "status": "fail" }
      user_session.is_logged_in = False
      
    if (user_session.blocked_at != None):
      blocked_at = datetime.fromisoformat(user_session.blocked_at)
      elapsed_time = datetime.now() - blocked_at
    
      if elapsed_time <= timedelta(minutes=1):
        return { "status_code": 401, "detail": "Usuario bloqueado. Intenta de nuevo en 15 minutos", "status": "fail" }
      user_session.blocked_at = None
      user_session.login_attempts = 0
    
    if (user_session.login_attempts >= 3):
      return { "status_code": 401, "detail": "Demasiados intentos fallidos al iniciar sesión", "status": "fail" }
    
    user_update = UserUpdate.from_session(user_session)
     
    if not bcrypt.checkpw(user.password.encode("utf-8"), user_session.password.encode("utf-8")):
      user_update.login_attempts += 1
      if user_update.login_attempts >= 3:
        user_update.blocked_at = str(datetime.now())
      self.user_service.update_session(user_update)
      return { "status_code": 401, "detail": "Credenciales invalidas", "status": "fail" }
    
    user_update.login_attempts = 0
    user_update.is_logged_in = True
    user_update.last_session = str(datetime.now())
    response = self.user_service.update_session(user_update)
    
    if response["status"] != "success":
      return response
    
    user_session = response["data"]
    user_read = UserRead.model_validate(user_session)
    user_token = UserToken.model_validate(user_read)
    token = await self.auth.create_token(user_token)
    
    # Creando la cookie de sesión
    cookie = {
      "key": "session",
      "value": token,
      "httponly": True,
      "secure": True,
      "samesite": "None",
      "max_age": self.auth.config.expiration_seconds
    }
    
    return { "message": "Incio de sesión exitoso", "status": "success", "cookie": cookie }
  
  async def logout(self):   
    token = self.user.token
    self.user.is_logged_in = False
    
    user_update = UserUpdate.from_token(self.user)
    self.user_service.update_session(user_update)
    
    await self.auth.invalidate_token(token)
    return { "message": "Sesión cerrada", "status": "success", "cookie": "close" }
  
  async def get_current_session(self):
    token = self.user.token
    cookie = {
      "key": "session",
      "value": token,
      "httponly": True,
      "secure": True,
      "samesite": "strict",
      "max_age": self.auth.config.expiration_seconds
    }
    return {  "message": "Sesión recuperada", "status": "success", "cookie": cookie }
    
SAuthDependency = Annotated[AuthService, Depends(AuthService)]