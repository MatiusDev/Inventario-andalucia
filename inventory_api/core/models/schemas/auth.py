from sqlmodel import SQLModel

import os

TOKEN_SECRET_KEY = os.getenv("SECRET_KEY")

class AuthenticationSettings(SQLModel):
  secret: str = TOKEN_SECRET_KEY
  jwt_algorithm: str = "HS256"
  expiration_seconds: int = 3600