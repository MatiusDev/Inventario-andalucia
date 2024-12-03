from sqlmodel import SQLModel

import os

SECRET_KEY = os.getenv("TOKEN_SECRET_KEY", "DEFAULT_SECRET_KEY")

class AuthenticationSettings(SQLModel):
  secret: str = SECRET_KEY
  jwt_algorithm: str = "HS256"
  expiration_seconds: int = 3600