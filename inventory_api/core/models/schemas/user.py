from sqlmodel import Field, SQLModel

from models.entities.user import User

# Esquemas de validación in/out de datos de usuario
class UserBase(SQLModel):
  username: str
  full_name: str
  email: str

# Un usuario DTO nuevo para BD o para registro en Auth
class UserCreate(UserBase):
  password: str

# Un usuario DTO ya existente en BD
class UserRead(UserBase):
  id: int
  type: str
  permissions: tuple
  active: bool
  is_logged_in: bool
  created_at: str
  updated_at: str
  last_session: str
  
  @staticmethod
  def from_db_user(user: User):
    def get_permissions(permissions: str):
      return tuple(permissions.split(" "))
   
    return UserRead(
      id = user.id,
      username = user.username,
      full_name = user.full_name,
      email = user.email,
      type = user.type,
      permissions = get_permissions(user.role.permissions),
      active = user.active,
      is_logged_in = user.is_logged_in,
      created_at = user.created_at.isoformat(),
      updated_at = user.updated_at.isoformat(),
      last_session = user.last_session.isoformat()
    )

# Usuario con Token para guardar la sesión
class UserToken(UserRead):
  token: str | None = Field(None)

class UserSession(UserRead):
  password: str | None
  login_attempts: int
  blocked_at: str | None
  
  @staticmethod
  def from_db_user(user: User):
    def get_permissions(permissions: str):
      return tuple(permissions.split(" "))
   
    return UserSession(
      id = user.id,
      username = user.username,
      full_name = user.full_name,
      email = user.email,
      password = user.password,
      type = user.type,
      permissions = get_permissions(user.role.permissions),
      active = user.active,
      is_logged_in = user.is_logged_in,
      login_attempts = user.login_attempts,
      blocked_at= user.blocked_at.isoformat() if user.blocked_at != None else None,
      created_at = user.created_at.isoformat(),
      updated_at = user.updated_at.isoformat(),
      last_session = user.last_session.isoformat()
    )

  @staticmethod
  def from_token(user: UserToken):
    return UserSession(
      id = user.id,
      username = user.username,
      full_name = user.full_name,
      email = user.email,
      type = user.type,
      permissions = user.permissions,
      active = user.active,
      is_logged_in = user.is_logged_in,
      created_at = user.created_at,
      updated_at = user.updated_at,
      last_session = user.last_session,
      password = None,
      login_attempts = 0
    )

class UserUpdate(UserBase):
  id: int | None
  password: str | None
  type: str | None
  permissions: tuple | None
  active: bool | None
  is_logged_in: bool | None
  login_attempts: int
  updated_at: str | None
  blocked_at: str | None
  last_session: str | None
  
  @staticmethod
  def from_read(user: UserRead):
    return UserUpdate(
      id=user.id,
      username=user.username,
      full_name=user.full_name,
      email=user.email,
      password=None,
      type=user.type,
      permissions=user.permissions,
      active=user.active,
      is_logged_in=user.is_logged_in,
      login_attempts=0,
      updated_at=user.updated_at,
      blocked_at=None,
      last_session=user.last_session
    )
    
  @staticmethod
  def from_session(user: UserSession):
    return UserUpdate(
      id=user.id,
      username=user.username,
      full_name=user.full_name,
      email=user.email,
      password=user.password,
      type=user.type,
      permissions=user.permissions,
      active=user.active,
      is_logged_in=user.is_logged_in,
      login_attempts=user.login_attempts,
      updated_at=user.updated_at,
      blocked_at=user.blocked_at,
      last_session=user.last_session
    )
  
  @staticmethod
  def from_base(user: UserBase):
    return UserUpdate(
      id=None,
      username=user.username,
      full_name=user.full_name,
      email=user.email,
      password=None,
      type=None,
      permissions=None,
      active=None,
      is_logged_in=None,
      login_attempts=0,
      updated_at=None,
      blocked_at=None,
      last_session=None
    )
  
  @staticmethod
  def from_token(user: UserToken):
    return UserUpdate(
      id=user.id,
      username=user.username,
      full_name=user.full_name,
      email=user.email,
      password=None,
      type=user.type,
      permissions=user.permissions,
      active=user.active,
      is_logged_in=user.is_logged_in,
      login_attempts=0,
      updated_at=user.updated_at,
      blocked_at=None,
      last_session=user.last_session
    )
  
  def update_dump(self, user: User):
    values = self.model_dump(exclude_none=True)
    values.pop('permissions', None)
    
    if values.get("blocked_at") == None:
      values["blocked_at"] = None
    print("HEEEEEEEEEEEEEEREEEEEEEEEEEEEE", values)
    
    for key, value in values.items():
      setattr(user, key, value)
    
    return values

# Usuario para login desde Front
class UserAuth(SQLModel):
  username: str
  password: str
