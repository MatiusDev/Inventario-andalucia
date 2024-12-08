from typing import Annotated
from fastapi import Depends
# Dependencias
from config.db_adapter import DBSession
from config.auth_token import UserDependency

from sqlalchemy.exc import IntegrityError
from sqlmodel import select
from datetime import datetime
# Entidades y esquemas
from models.entities.user import User
from models.schemas.user import UserBase, UserRead, UserSession, UserCreate, UserUpdate
from models.enums.role import RoleType, Permissions

class UserService:
  def __init__(self, db: DBSession, user: UserDependency) -> None:
    self.db = db
    self.user = user
  
  # User services http methods
  
  async def get_all(self):
    try:
      if (self.user.type == RoleType.USER
          or Permissions.READ not in self.user.permissions):
        return { "status_code": 403, "detail": "No tienes permisos para acceder a este recurso", "status": "fail" }
     
      users_db = self.db.exec(select(User)).all()
      users = [UserRead.from_db_user(user) for user in users_db]
      
      return { "data" : users, "status": "success" }
    except Exception as err:
      return { "status_code": 500, "detail": str(err), "status": "error"}
  
  async def get(self, id: int):     
    if (self.user.type == RoleType.USER and self.user.id != id
      or Permissions.READ not in self.user.permissions):
      return { "status_code": 403, "detail": "No tiene permisos para acceder a este recurso", "status": "fail" }
    
    response = self.get_by_id(id)
    
    if response["status"] != "success":
      return response
    
    user_db = response["data"]
    read_user = UserRead.from_db_user(user_db)
    return { "data": read_user, "status": "success" }

  async def create(self, user: UserCreate):
    if (self.user.type == RoleType.USER
          or Permissions.EDIT not in self.user.permissions):
        return { 
          "status_code": 403, 
          "detail": "No tienes permisos para acceder a este recurso",
          "status": "fail"
        }
    return self.create_user(user)

  # Crear logica de actualización
  async def update(self, id: int, user: UserBase):   
    if (self.user.type == RoleType.USER and self.user.id != id 
      or self.user.type == RoleType.ADMIN and Permissions.EDIT not in self.user.permissions):
        return { 
          "status_code": 403, 
          "detail": "No tiene permisos para acceder a este recurso", 
          "status": "fail"
        }
    
    user_update = UserUpdate.from_base(user)
    response = self.update_user(id, user_update)
    
    if response["status"] != "success":
      return response
    
    user_db = response["data"]
    user_read = UserRead.from_db_user(user_db)
    return { "data": user_read, "status": "success" }
    
  async def delete(self, id: int):
    try:   
      if (self.user.type == RoleType.USER
        or Permissions.DELETE not in self.user.permissions):
          return { 
            "status_code": 403,
            "detail": "No tienes permisos para acceder a este recurso",
            "status": "fail"
          }
      
      user_db = self.db.get(User, id)
      
      if user_db == None:
        return { "status_code": 404, "detail": "Usuario no encontrado", "status": "fail" }
      
      user_db.active = False
      user_db.updated_at = datetime.now()
      self.db.commit()
      return { "message": "Usuario inactivado correctamente", "status": "success" }
    except Exception as err:
      return { "status_code": 500, "detail": str(err), "status": "error" }
  
  # User services methods
  def get_by_id(self, id: int) -> User:
    try:
      user_db = self.db.get(User, id)
      
      if user_db == None:
        return { "status_code": 404, "detail": "Usuario no encontrado", "status": "fail" }
      
      return { "data": user_db, "status": "success" }
    except Exception as err:
      return {  "status_code": 500, "detail": str(err), "status": "error" }
  
  def get_by_username(self, username: str) -> User:
    try:
      user_db = self.db.exec(select(User).where(User.username == username)).first()
      
      if user_db == None:
        return { "status_code": 404, "detail": "No se ha encontrado el usuario", "status": "fail" }
      
      return { "status_code": 200, "data": user_db, "status": "success" }
    except Exception as err:
      return { "status_code": 500, "detail": str(err), "status": "error" }
  
  def get_by_email(self, email: str):
    pass
  
  def update_user(self, id: int, user: UserUpdate):
    try:
      user_db = self.db.get(User, id)

      if user_db == None:
        return { "status_code": 404, "detail": "Usuario no encontrado", "status": "fail" }
      
      user_updated = user.update_dump(user_db)
      user_db.sqlmodel_update(user_updated)
      
      self.db.add(user_db)
      self.db.commit()
      self.db.refresh(user_db)
      
      return { "data": user_db, "status": "success" }
    except Exception as err:
      return {  "status_code": 500, "detail": str(err), "status": "error" }
  
  def create_user(self, user: UserCreate):
    try:
      new_user = User.model_validate(user.model_dump())
      self.db.add(new_user)
      self.db.commit()
      self.db.refresh(new_user)
            
      user_read = UserRead.from_db_user(new_user)
      return { "data": user_read, "status": "success" }
    except Exception as err:
      self.db.rollback()
      if not hasattr(err, "orig"):
        return {  "status_code": 500, "detail": str(err), "status": "error" }  
      err_id, err_msg = err.orig.args
      
      if "unique_username" in str(err.orig) or "unique_email" in str(err.orig):
        return { "status_code": 400, "detail": "El usuario o correo ya existe", "status": "fail" }
      
      if err_id == 1452:
        return { 
          "status_code": 500,
          "detail": "No se ha creado ningún rol en la base de datos",
          "status": "fail" 
        }
      
      return { "status_code": 500, "detail": str(err_msg), "status": "error" }
  
  def get_session(self, id: int = None, username: str = None, email: str = None):
    if id != None:
      response = self.get_by_id(id)
    elif username != None:
      response = self.get_by_username(username)
    elif email != None:
      response = self.get_by_email(email)
    else:
      return { "status_code": 500, "detail": "No se puede traer la sesión del usuario", "status": "error" }
    
    if response["status"] != "success":
      return response
    
    user_db = response["data"]
    user_session = UserSession.from_db_user(user_db)
    
    return { "data": user_session, "status": "success" }

  def update_session(self, user: UserUpdate):
    response = self.update_user(user.id, user)
    
    if response["status"] != "success":
      return response
    
    user_db = response["data"]
    user_session = UserSession.from_db_user(user_db)
    return { "data": user_session, "status": "success" }

SUserDependency = Annotated[UserService, Depends(UserService)]