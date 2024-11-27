# from typing import Annotated, Any
# from fastapi import Depends
# from fastapi_auth_jwt import JWTAuthBackend

# from models.schemas.auth import AuthenticationSettings
# from models.schemas.user import RegisterUser as User

# class AuthBackend:
#   def __init__(self) -> None:
#     self.auth = JWTAuthBackend(
#       authentication_config=AuthenticationSettings(),
#       user_schema=User
#     )

#   def __call__(self) -> Any:
#     return self.auth

# AuthDependency = Annotated[JWTAuthBackend, Depends(AuthBackend)]

# from typing import Annotated
# from fastapi import Depends
from fastapi_auth_jwt import JWTAuthBackend
from pydantic import BaseModel, Field

from models.schemas.auth import AuthenticationSettings
# from models.schemas.user import User

class User(BaseModel):
  username: str
  password: str
  token: str | None = Field(None)

auth_backend = JWTAuthBackend(
  authentication_config=AuthenticationSettings(),
  user_schema=User
)

# AuthDependency = Annotated[JWTAuthBackend, Depends(auth_backend)]