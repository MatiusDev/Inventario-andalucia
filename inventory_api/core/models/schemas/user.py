# from sqlmodel import SQLModel
from pydantic import BaseModel

class LoginUser(BaseModel):
  username: str
  password: str
  
# class RegisterUser(User):
#   token: str = Field(None)
#   pass