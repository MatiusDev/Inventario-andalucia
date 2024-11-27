from typing import Annotated
from fastapi import Depends

# from config.auth_token import AuthDependency
from config.auth_token import auth_backend

from models.schemas.user import LoginUser

class AuthService:
  def __init__(self) -> None:
    # self.auth = auth
    pass
    
  async def login(self, user: LoginUser):
    print("Here in print user", user)
    token = await auth_backend.create_token(user)
    print("Here in print token", token)
    return { "token": token }
    
SAuthDependency = Annotated[AuthService, Depends(AuthService)]