from fastapi import APIRouter

from models.schemas.supplier import SupplierCreate

from services.supplier_service import SSupplierDependency

from utils.response_handler import response_handler

route = APIRouter()

@route.get("/", status_code=200)
async def get_all_orders(supplier_service: SSupplierDependency):
  return await response_handler(supplier_service.get_all())

@route.get("/{id}", status_code=200)
async def get_supplier(id: int, supplier_service: SSupplierDependency):
  return await response_handler(supplier_service.get_by_id(id))
  
@route.post("/", status_code=201)
async def create_supplier(supplier: SupplierCreate, supplier_service: SSupplierDependency):
  return await response_handler(supplier_service.create(supplier))

@route.put("/{id}", status_code=200)
async def update_supplier(id: int, supplier: SupplierCreate, supplier_service: SSupplierDependency):
  return await response_handler(supplier_service.update(id, supplier))

@route.delete("/{id}", status_code=200)
async def delete_supplier(id: int, supplier_service: SSupplierDependency):
  return await response_handler(supplier_service.delete(id))
