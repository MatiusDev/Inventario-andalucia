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

<<<<<<< HEAD
app.add_middleware(
  CORSMiddleware,
  allow_origins=config["origins"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)
app.add_middleware(CheckOriginMiddleware, allowed_origins=config["origins"])

app.include_router(routes, prefix="/api")


=======
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/Insult")
def read_insult():
    return {"Fuck": "World"}
@app.get("/saludo")
def say_hello():
    return {"Hello": "World"}

@app.get("/product")
def read_product():
    return {"producto": "planta"}

@app.get("/adios")
def say_bye():
    return {"bye": "World"}
  
@app.get("/transfer")
def read_product():
    return {"Medio de pago": "efectivo"}
>>>>>>> 9954187ed3c1fca89062d6c6f069883449470e9c
