from typing import Union

from fastapi import FastAPI

app = FastAPI()

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

@app.get("/transfer")
def read_product():
    return {"Medio de pago": "efectivo"}
