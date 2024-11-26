from fastapi import APIRouter, Depends

from models.schemas.product import ProductCreate

from services.product_service import ProductService

route = APIRouter()

@route.get("/{id}")
def get_product(id: int, product_service: ProductService = Depends(ProductService)):
  return product_service.get_user_by_id(id)
  
@route.post("/")
def create_product(product: ProductCreate, product_service: ProductService = Depends(ProductService)):
  return product_service.new_product(product)

@route.put("/{id}")
def update_product(id: int, product: ProductCreate, product_service: ProductService = Depends(ProductService)):
  return product_service.update_product(id, product)

@route.delete("/{id}")
def delete_product(id: int, product_service: ProductService = Depends(ProductService)):
  return product_service.delete_product(id)