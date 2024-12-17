import os

from core.config.db_adapter import DBAdapter
from core.config.auth_token import AuthBackend
from tenacity import retry, wait_fixed, stop_after_attempt

config = {
  "environment": None,
  "origins": [],
  "auth": None
}

def environment_config():
  '''Esta función realiza la configuración general del ambiente que se está ejecutando.
  '''
  try:
    environments = [
      "development",
      "production"
    ]
    env = os.getenv("ENVIRONMENT")
        
    if env not in environments or env is None:
      raise Exception(f"El ambiente de trabajo {env} de la variable de entorno ENVIRONMENT no es soportado.")
    
    db_config(env)
    
    config["environment"] = env
    config["origins"] = cors_origins_config(env)
    config["auth"] = AuthBackend()
    
    return config
  except Exception as err:
    print(f"Ha ocurrido un error inesperado: {err}")
    return config
          
def db_config(env: str):
  echo = True
  if env == 'development':
    echo = True
  
  db_driver = os.getenv("DB_DRIVER", "mysql")
  if db_driver == "mysql":
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    driver_connection = f"mysql+mysqldb://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    return connect_db(driver_connection, echo)
  else:
    raise Exception(f"El motor de base de datos {db_driver} no es soportado.")

@retry(wait=wait_fixed(5), stop=stop_after_attempt(3))
def connect_db(driver_connection: str, echo: bool = False):
  try:
    print("Conectando a la base de datos...")
    db_adapter = DBAdapter(db_driver=driver_connection, echo=echo)
    if db_adapter.get_session() is None:
      raise Exception("Error al conectar a la base de datos")
    db_adapter.create_initial_tables()
    print("Conexión exitosa a la base de datos")
    return
  except Exception as err:
    raise Exception(f"Error al conectar a la base de datos: {err}")

def cors_origins_config(env: str):
  origins = ["http://localhost:5173", "http://127.0.0.1:5173"]

  if env == 'production':
    HOST_FRONTEND_URL = os.getenv("HOST_FRONTEND_URL")
    origins = [HOST_FRONTEND_URL]
  return origins
