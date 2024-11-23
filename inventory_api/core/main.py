import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

#Configuraciones
from config.environtment import config_environment

#Middlewares
from middlewares.check_origin_middleware import CheckOriginMiddleware

#Router
from routers.index import routes

load_dotenv()

env = os.getenv("ENVIRONMENT")

config_environment(env)

app = FastAPI()

origins = {"*"}

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)
app.add_middleware(CheckOriginMiddleware, allowed_origins=origins)

app.include_router(routes, prefix="/api")


