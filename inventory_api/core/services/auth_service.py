from typing import Annotated
from fastapi import Depends, HTTPException
import bcrypt

from models.schemas.user import UserAuth, UserRegister, UserToken, UserCreate

from config.auth_token import AuthDependency

from services.user_service import SUserDependency

class AuthService:
  def __init__(self, auth: AuthDependency, user: SUserDependency) -> None:
    self.auth = auth
    self.user = user
  
  async def sign_up(self, user: UserRegister):
    hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())
    
    user_create = UserCreate(
      username=user.username,
      password=hashed_password,
      full_name=user.full_name,
      email=user.email
    )
    user_read = self.user.create(user_create)
    
    user_token = UserToken(
      id=user_read.id,
      username=user_read.username,
      full_name=user_read.full_name,
      email=user_read.email,
      role=user_read.role,
      active=user_read.active,
      created_at=user_read.created_at,
      updated_at=user_read.updated_at,
      last_session=user_read.last_session
    )
    token = await self.auth.create_token(user_token)
        
    return { "token": token, "status": "success" }
  
  async def login(self, user: UserAuth):
    user_read = self.user.get_by_username(user.username)
    
    if user_read == None:
      raise HTTPException(status_code=404, detail="No se ha encontrado el usuario")
    
    if not bcrypt.checkpw(user.password.encode("utf-8"), user_read.password.encode("utf-8")):
      raise HTTPException(status_code=401, detail="Credenciales invalidas")
    
    user_token = UserToken(
      id=user_read.id,
      username=user_read.username,
      full_name=user_read.full_name,
      email=user_read.email,
      role=user_read.role,
      active=user_read.active,
      created_at=user_read.created_at,
      updated_at=user_read.updated_at,
      last_session=user_read.last_session
    )
    token = await self.auth.create_token(user_token)
        
    return { "token": token, "status": "success" }
  
  async def logout(self, user: UserToken):
    self.auth.invalidate_token(user)
    return { "status": "success" }
    
SAuthDependency = Annotated[AuthService, Depends(AuthService)]