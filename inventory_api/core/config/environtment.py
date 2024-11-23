import os

from .db_adapter import DBAdapter

def config_environment(enviroment: str):
  '''Esta función me devuelve la configuración del ambiente
  recibido como parámetro.
  
  Parámetros:
  enviroment: str -> Enviar 'development' o 'production' como opción.
  '''
  echo = False
  if enviroment == 'development':
    echo = True
    
  if os.getenv("DB_DRIVER", "mysql") == "mysql":
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_driver = f"mysql+mysqldb://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    
    try:
      db_adapter = DBAdapter(db_driver=db_driver, echo=echo)
      print("Conectando a la base de datos...")
      db_adapter.create_initial_tables()
    except Exception as e:
      print(e)
    
  
  
  