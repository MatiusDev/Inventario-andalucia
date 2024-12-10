from typing import Annotated
from fastapi import Depends
# Dependencias
from config.db_adapter import DBSession

from sqlmodel import select
# Entidades y esquemas
from models.entities.supplier import Supplier
from models.schemas.supplier import SupplierBase, SupplierCreate, SupplierRead, SupplierUpdate

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
  
  async def update(self, id: int, supplier: SupplierUpdate):
    try:
      supplier_db = self.db.get(Supplier,id)
      if supplier_db == None:
        return { "status_code": 404, "detail": "Supplier not found", "status": "fail" }
      
      supplier_db_dict = supplier.model_dump(exclude_unset=True)

      supplier_db.sqlmodel_update(supplier_db_dict)
      self.db.add(supplier_db)
      self.db.commit()
      self.db.refresh(supplier_db)

    except Exception as err:
      return {  "status_code": 500, "detail": str(err), "status": "error" }
    
    print(supplier_db)

    return { "data": "Proveedor actualizado con éxito", "status": "success" }
  
  async def delete(self, id: int):
    try:
      supplier_db = self.db.get(Supplier,id)
      if supplier_db == None:
        return { "status_code": 404, "detail": "Supplier not found", "status": "fail" }
      self.db.delete(supplier_db)
      self.db.commit()
      return {"message": "Proveedor eliminado", "status": "success"}
    
    except Exception as err:
      return {  "status_code": 500, "detail": str(err), "status": "error" }
  
SSupplierDependency = Annotated[SupplierService, Depends(SupplierService)]