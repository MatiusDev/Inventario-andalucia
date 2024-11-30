from typing import Annotated
from fastapi import Depends

from fastapi_auth_jwt import JWTAuthBackend

from models.schemas.auth import AuthenticationSettings
from models.schemas.user import UserToken

class AuthBackend(JWTAuthBackend): 
  def __init__(self):
    super().__init__(
      authentication_config=AuthenticationSettings(), 
      user_schema=UserToken
    )
    
AuthDependency = Annotated[AuthBackend, Depends(AuthBackend)]