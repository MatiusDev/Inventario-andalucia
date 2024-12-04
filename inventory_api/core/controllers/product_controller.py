from fastapi import APIRouter

from models.schemas.product import ProductCreate, ProductRead

from services.product_service import SProductDependency

route = APIRouter()

@route.get("/")
def get_all_products(product_service: SProductDependency):
  return product_service.get_all()

@route.get("/{id}")
def get_product(id: int, product_service: SProductDependency):
  return product_service.get_by_id(id)
  
@route.post("/", response_model=ProductRead)
def create_product(product: ProductCreate, product_service: SProductDependency):
  return product_service.create(product)

# @route.put("/{id}")
# def update_product(id: int, product: ProductCreate, product_service: SProductDependency):
#   return product_service.update_product(id, product)

# @route.delete("/product/{id}")
# def delete_product(id: int, product_service: SProductDependency):
#   return product_service.delete_product(id)