from sqlmodel import SQLModel

from models.entities.supplier import Supplier

class SupplierBase(SQLModel):
  name: str
  email: str
  address: str
  city: str

class SupplierCreate(SupplierBase):
  phone: str | None = None
  pass

class SupplierRead(SupplierBase):
  id: int | None
  phone: str | None
  active: bool
  
  @staticmethod
  def from_db(supplier: Supplier):
    return SupplierRead(
      id=supplier.id,
      name=supplier.name,
      email=supplier.email,
      address=supplier.address,
      city=supplier.city,
      phone=supplier.phone,
      active=supplier.active
    )

# Recordar usar el dump, para no tener que hacer traducciones
class SupplierUpdate(SupplierBase):
  id: int | None
  phone: str | None
  active: bool | None