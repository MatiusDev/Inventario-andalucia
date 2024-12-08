from sqlmodel import SQLModel

import os

SECRET_KEY = os.getenv("TOKEN_SECRET_KEY", "DEFAULT_SECRET_KEY")
ALGORITHM = os.getenv("TOKEN_ALGORITHM", "HS256")
EXP_TIME = os.getenv("TOKEN_EXP_TIME", 5400)

class AuthenticationSettings(SQLModel):
  secret: str = SECRET_KEY
  jwt_algorithm: str = ALGORITHM
  expiration_seconds: int = EXP_TIME