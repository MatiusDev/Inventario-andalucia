from fastapi import APIRouter

from models.schemas.product import ProductCreate, ProductRead

from services.product_service import SProductDependency

route = APIRouter()

@route.get("/", status_code=200)
def get_all_products(product_service: SProductDependency):
  return product_service.get_all()

@route.get("/supplies/", status_code=200)
async def get_all_supplies(product_service: SProductDependency):
    return await product_service.get_all_supplies()

@route.get("/{id}", status_code=200)
def get_product(id: int, product_service: SProductDependency):
  return product_service.get_by_id(id)
  
@route.post("/", status_code=201)
def create_product(product: ProductCreate, product_service: SProductDependency):
  return product_service.create(product)

# @route.put("/{id}")
# def update_product(id: int, product: ProductCreate, product_service: SProductDependency):
#   return product_service.update_product(id, product)

# @route.delete("/product/{id}")
# def delete_product(id: int, product_service: SProductDependency):
#   return product_service.delete_product(id)