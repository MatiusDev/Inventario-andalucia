from fastapi import Depends
from sqlmodel import Session

from routers.product_router import product_router as route
from views.product_view import ProductView
from models.product import Product
from config.db_adapter import DBAdapter

@route.get("/",)
def get_product(db = Depends(DBAdapter.get_session)):
    product = {}
    return ProductView.get_product(product)
  
@route.post("/")
def create_product(product: Product, db: Session = Depends(DBAdapter.get_session)):
  db.add(product)
  db.commit()
  return ProductView.create_product(product)


@route.put("/")
def update_product():
  pass

@route.delete("/")
def delete_product():
  pass