from typing import Annotated
from fastapi import Depends, HTTPException

from config.db_adapter import DBSession

from sqlmodel import select

from models.entities.user import User
from models.schemas.user import UserCreate, UserRead
from models.enums.role import Role as ROLES

class UserService:
  def __init__(self, db: DBSession) -> None:
    self.db = db
  
  def get_all(self):
    pass
  
  def get_by_username(self, username: str):
    user = self.db.exec(select(User).where(User.username == username)).first()
    
    if user == None:
      return { "status_code": 404, "detail": "No se ha encontrado el usuario", "status": "fail" }
    
    user_read = UserRead.from_user(user)
    return { "status_code": 200, "data": (user_read, user.password), "status": "success" }
  
  def get_by_id(self, id: int):
    pass

  def create(self, user: UserCreate) -> UserRead:
    new_user = User.model_validate(user.model_dump())
    
    self.db.add(new_user)
    self.db.commit()
    print("antes", new_user)
    self.db.refresh(new_user)
    print("despues", new_user)
    user_read = UserRead.from_user(new_user)
    return user_read

  def update(self, id: int, user: UserCreate):
    pass

  def delete(self, id: int):
    pass
  
SUserDependency = Annotated[UserService, Depends(UserService)]