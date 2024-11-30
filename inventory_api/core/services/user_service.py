from typing import Annotated
from fastapi import Depends, HTTPException

from config.db_adapter import DBSession

from sqlmodel import select

from models.entities.user import User
from models.schemas.user import UserCreate, UserRead, UserAuthRead
from models.enums.role import Role as ROLES

class UserService:
  def __init__(self, db: DBSession) -> None:
    self.db = db
  
  def get_all(self):
    pass
  
  def get_by_username(self, username: str) -> UserAuthRead | None:
    user = self.db.exec(select(User).where(User.username == username)).first()
    
    if user == None:
      return None
    
    user_read = UserAuthRead(
      id=user.id,
      username=user.username,
      password=user.password,
      role="common",
      full_name=user.full_name,
      email=user.email,
      active=user.active,
      created_at=user.created_at,
      updated_at=user.updated_at,
      last_session=user.last_session
    )
    
    return user_read
  
  def get_by_id(self, id: int):
    pass

  def create(self, user: UserCreate):
    default_role = ROLES.ADMIN.value # Administrador --> Cambiar estructura por enum
    
    new_user = User(
      username=user.username,
      password=user.password,
      full_name=user.full_name,
      email=user.email,
      role_id=default_role
    )
    
    try:
      self.db.add(new_user)
      self.db.commit()
      self.db.refresh(new_user)
    except Exception as e:
      raise HTTPException(status_code=500, detail=str(e))
    
    user_read = UserRead(
      id=new_user.id,
      username=new_user.username,
      full_name=new_user.full_name,
      email=new_user.email,
      role=ROLES.ADMIN.name,
      active=new_user.active,
      created_at=new_user.created_at,
      updated_at=new_user.updated_at,
      last_session=new_user.last_session
    )
        
    return user_read

  def update(self, id: int, user: UserCreate):
    pass

  def delete(self, id: int):
    pass
  
SUserDependency = Annotated[UserService, Depends(UserService)]
    