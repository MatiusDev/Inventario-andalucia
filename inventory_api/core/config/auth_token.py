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
  
  @staticmethod    
  def get_user(request: Request) -> UserToken | None:
    if not hasattr(request, "state") or not hasattr(request.state, "user"):
      return None
    
    return request.state.user
  
    
AuthDependency = Annotated[AuthBackend, Depends(AuthBackend)]
UserDependency = Annotated[UserToken, Depends(AuthBackend.get_user)]