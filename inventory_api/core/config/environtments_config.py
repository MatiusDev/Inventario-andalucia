import os

from core.config.db_adapter import DBAdapter
from core.config.auth_token import AuthBackend

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
  echo = False
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
    print(driver_connection)
  else:
    raise Exception(f"El motor de base de datos {db_driver} no es soportado.")
    
  print("Conectando a la base de datos...")
  DBAdapter(db_driver=driver_connection, echo=echo)
  


def cors_origins_config(env: str):
  origins = ["*"]

  if env == 'production':
    FRONTEND_URL = os.getenv("FRONTEND_URL")
    origins = [FRONTEND_URL]
  return origins