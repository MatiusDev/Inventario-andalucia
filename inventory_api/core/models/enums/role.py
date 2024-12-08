from enum import Enum

# Agregar en la base de datos estos roles en ese orden.
class RoleID(Enum):
  USER = 1
  ADMIN = 2

class RoleType(str, Enum):
  USER = "Usuario"
  ADMIN = "Administrador"
  
class Permissions(str, Enum):
  READ = "READ"
  EDIT = "EDIT"
  DELETE = "DELETE"