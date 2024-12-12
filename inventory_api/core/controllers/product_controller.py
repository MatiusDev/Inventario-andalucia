from fastapi import APIRouter

from core.models.schemas.product import ProductCreate, ProductUpdate

from core.services.product_service import SProductDependency
from core.utils.response_handler import response_handler

route = APIRouter()

@route.get("/", status_code=200)
async def get_all_products(product_service: SProductDependency):
  return await response_handler(product_service.get_all())

@route.get("/supplies", status_code=200)
async def get_all_supplies(product_service: SProductDependency):
    return await response_handler(product_service.get_all_supplies())

@route.get("/{id}", status_code=200)
def get_product(id: int, product_service: SProductDependency):
  return product_service.get_by_id(id)
  
@route.post("/", status_code=201)
def create_product(product: ProductCreate, product_service: SProductDependency):
  return product_service.create(product)

@route.put("/{id}")
def update_product(id: int, product: ProductUpdate, product_service: SProductDependency):
  return product_service.update(id, product)

@route.delete("/{id}")
def delete_product(id: int, product_service: SProductDependency):
  return product_service.delete(id)