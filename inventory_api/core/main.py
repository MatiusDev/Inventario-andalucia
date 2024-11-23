import os

from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

#Configuraciones
from config.environtment import config_environment

#Router
from routers.index import routes


load_dotenv()

env = os.getenv("ENVIRONMENT")

config_environment(env)

app = FastAPI()

app.include_router(routes, prefix="/api")


