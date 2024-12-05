from typing import Annotated
from fastapi import Depends, Request
# Dependencias
from config.db_adapter import DBSession
from config.auth_token import AuthDependency

from sqlalchemy.exc import IntegrityError
from sqlmodel import select
from datetime import datetime
# Entidades y esquemas
from models.entities.user import User
from models.schemas.user import UserCreate, UserRead, UserUpdate
from models.enums.role import RoleType, Permissions

class UserService:
  def __init__(self, db: DBSession, auth: AuthDependency, request: Request) -> None:
    self.db = db
    self.auth = auth
    self.request = request
  
  async def get_all(self):
    try:
      user = await self.auth.get_user(self.request)
      
      if (user.role == RoleType.USER
          or Permissions.READ not in user.permissions):
        return { "status_code": 403, "detail": "No tienes permisos para acceder a este recurso", "status": "fail" }
     
      users_db = self.db.exec(select(User)).all()
      users = [UserRead.from_user(user) for user in users_db]
      
      return { "data" : users, "status": "success" }
    except Exception as err:
      return { "status_code": 500, "detail": str(err), "status": "error"}
  
  def get_by_username(self, username: str):
    try:
      user_db = self.db.exec(select(User).where(User.username == username)).first()
      
      if user_db == None:
        return { "status_code": 404, "detail": "No se ha encontrado el usuario", "status": "fail" }
      
      user_read = UserRead.from_user(user_db)
      return { "status_code": 200, "data": (user_read, user_db.password), "status": "success" }
    except Exception as err:
      print("HERE IN EXCEPTION")
      return { "status_code": 500, "detail": str(err), "status": "error" }
  
  async def get_by_id(self, id: int):
    user = await self.auth.get_user(self.request)
      
    if (user.role == RoleType.USER and user.id != id
      or Permissions.READ not in user.permissions):
      return { "status_code": 403, "detail": "No tiene permisos para acceder a este recurso", "status": "fail" }
      
    user_db = self.db.get(User, id)
    
    if user_db == None:
      return { "status_code": 404, "detail": "Rol no encontrado", "status": "fail" }
    
    read_user = UserRead.from_user(user_db)
    return { "data": read_user, "status": "success" }

  async def create(self, user: UserCreate):
    try:
      new_user = User.model_validate(user.model_dump())
      self.db.add(new_user)
      self.db.commit()
      self.db.refresh(new_user)
            
      user_read = UserRead.from_user(new_user)
      return { "data": user_read, "status": "success" }
    except Exception as err:
      self.db.rollback()
      err_id, err_msg = err.orig.args
      
      if "unique_username" in str(err.orig) or "unique_email" in str(err.orig):
        return { "status_code": 400, "detail": "El usuario o correo ya existe", "status": "fail" }
      
      if err_id == 1452:
        return { "status_code": 500, "detail": "No se ha creado ningún rol en la base de datos", "status": "fail" }
      
      return { "status_code": 500, "detail": str(err_msg), "status": "error" }

  # Crear logica de actualización
  async def update(self, id: int, user: UserUpdate):
    try:
      user_db = self.db.get(User, id)

      if user_db == None:
        return { "status_code": 404, "detail": "Rol no encontrado", "status": "fail" }
      
      # user_db.full_name = user.full_name if user.full_name != None else user_db.full_name
      # user_db.email = user.email if user.email != None else user_db.email
      # user_db.password = user.password if user.password != None else user_db.password
      # user_db.role = user.role if user.role != None else user_db.role
      # full_name: str | None
      # email: str | None
      # password: str | None
      # role: str | None
      # active: bool | None
      # updated_at: str | None
      # last_session: str | None
      self.db.add(user_db)
      self.db.commit()
      self.db.refresh(user_db)
      
      read_user = UserRead.model_validate(user_db)
      return { "data": read_user, "status": "success" }
    except Exception as err:
      return {  "status_code": 500, "detail": str(err), "status": "error" }

  def update_login_attempts(self, id: int):
    pass
  
  def update_last_session(self, id: int):
    pass

  async def delete(self, id: int):
    try:
      user = await self.auth.get_user(self.request)
    
      if (user.role == RoleType.USER
      or Permissions.DELETE not in user.permissions):
        return { "status_code": 403, "detail": "No tienes permisos para acceder a este recurso", "status": "fail" }
      
      user_db = self.db.get(User, id)
      
      if user_db == None:
        return { "status_code": 404, "detail": "Usuario no encontrado", "status": "fail" }
      
      user_db.active = False
      user_db.updated_at = datetime.now()
      self.db.commit()
      return { "message": "Usuario inactivado", "status": "success" }
    except Exception as err:
      return { "status_code": 500, "detail": str(err), "status": "error" }
  
SUserDependency = Annotated[UserService, Depends(UserService)]