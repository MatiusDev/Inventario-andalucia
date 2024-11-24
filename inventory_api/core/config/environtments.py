import os

from .db_adapter import DBAdapter

def config_environment():
  '''Esta función realiza la configuración general del ambiente que se está ejecutando.
  '''
  try:
    environments = [
      "development",
      "production"
    ]
    env = os.getenv("ENVIRONMENT")
        
    if env not in environments:
      raise Exception(f"El ambiente de trabajo {env} de la variable de entorno ENVIRONMENT no es soportado.")
    
    config_database(env)
    
    return {
      "environment": env,
      "origins": config_cors_origins(env)
    }
  except Exception as err:
    print(f"Ha ocurrido un error inesperado: {err}")
    return {
      "environment": None,
      "origins": []
    }
          
def config_database(env: str):
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
  else:
    raise Exception(f"El motor de base de datos {db_driver} no es soportado.")
    
  print("Conectando a la base de datos...")
  db_adapter = DBAdapter(db_driver=driver_connection, echo=echo)
  db_adapter.create_initial_tables()

def config_cors_origins(env: str):
  origins = ["http://localhost:5173"]

  if env == 'production':
    FRONTEND_URL = os.getenv("FRONTEND_URL")
    origins = [FRONTEND_URL]
  return origins
    
  
  
  