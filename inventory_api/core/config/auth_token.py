from typing import Annotated
from fastapi import Depends, Request

from fastapi_auth_jwt import JWTAuthBackend

from models.schemas.auth import AuthenticationSettings
from models.schemas.user import UserToken

class AuthBackend(JWTAuthBackend): 
  def __init__(self):
    super().__init__(
      authentication_config=AuthenticationSettings(), 
      user_schema=UserToken
    )
    
  async def get_user(self, request: Request) -> UserToken:
    auth = request.headers.get("Authorization")
    token = auth.split(" ")[1]
    return await super().get_current_user(token)
    
AuthDependency = Annotated[AuthBackend, Depends(AuthBackend)]