from sqlmodel import SQLModel, create_engine, Session
from typing import Annotated
from fastapi import Depends

class DBAdapter:
  _instance = None
  _engine = None
  _session = None
  
  # Método para crear una nueva instancia de la clase
  # Debido a que es una BD, quiero usar el patrón singleton para devolver una única instancia de la clase que esta conectada al motor de la BD.
  def __new__(cls, db_driver: str = None, connect_args: dict = {}, echo: bool = False):
    if cls._instance is None:
      cls._instance = super().__new__(cls)
      # Me permite crear una instancia con el motor de base de datos (db_driver) que me llegue por parámetro (Mysql, Postgres, etc)
      cls._engine = create_engine(
        db_driver,
        connect_args=connect_args,
        echo=echo)
    return cls._instance
  
   # Los classmethod, son clases del metodo tal cual como se traduce, me permite manejar los parametros declarados en la clase, accediendo desde cls (parecido a self), como es una única instancia para usar los parametros globales necesito a cls en los métodos
  @classmethod
  def create_initial_tables(cls):
    if cls._engine is None:
      raise Exception("El motor de base de datos no está configurado")
    
    SQLModel.metadata.create_all(cls._engine)
  
  @classmethod
  def get_session(cls):
    if cls._engine is None:
      raise Exception("El motor de base de datos no está configurado")
  
  # Este with me permite manejar las sesiones con un ciclo de vida, cuando se ha usado el generador yield, es decir, me trae la sesión para interactuar con la bd, y si termina el bloque de código donde se está usando la sesión, esta se cierra automáticamente.  
    with Session(cls._engine) as session:
      yield session

# Esta variable permite exportar la sesión de la base de datos para integrar como dependencia en las consultas de los endpoints
SessionDep = Annotated[Session, Depends(DBAdapter.get_session)]