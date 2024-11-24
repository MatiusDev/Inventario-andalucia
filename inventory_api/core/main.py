import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv

#Configuraciones
from config.environtments import config_environment

#Middlewares
from middlewares.check_origin_middleware import CheckOriginMiddleware

#Router
from routers.index import routes

load_dotenv()

config = config_environment()

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=config["origins"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)
app.add_middleware(CheckOriginMiddleware, allowed_origins=config["origins"])

app.include_router(routes, prefix="/api")


