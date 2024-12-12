from typing import Annotated
from fastapi import Depends
from sqlmodel import select
# Dependencias
from core.config.db_adapter import DBSession

# Entidades y esquemas
from core.models.entities.supplier import Supplier
from core.models.schemas.supplier import SupplierBase, SupplierCreate, SupplierRead

class SupplierService:
  def __init__(self, db: DBSession) -> None:
    self.db = db
    
  async def get_all(self):
    suppliers_db = self.db.exec(select(Supplier)).all() or []
    suppliers = [SupplierRead.from_db(supplier) for supplier in suppliers_db]
    
    return { "data" : suppliers, "status": "success" }
  
  async def get_by_id(self, id: int):
    supplier = self.db.get(Supplier, id)
    
    if supplier == None:
      return { "status_code": 404, "detail": "Supplier not found", "status": "fail" }
    
    read_supplier = SupplierRead.from_db(supplier)
    return { "data": read_supplier, "status": "success"}
  
  async def create(self, supplier: SupplierCreate):
    supplier_db = Supplier.model_validate(supplier)
    self.db.add(supplier_db)
    self.db.commit()
    self.db.refresh(supplier_db)
    
    read_supplier = SupplierRead.from_db(supplier_db)
    return { "data": read_supplier, "status": "success" }
  
  async def update(self, id: int, supplier: SupplierBase):
    pass
  
  async def delete(self, id: int):
    pass
  
SSupplierDependency = Annotated[SupplierService, Depends(SupplierService)]