from sqlmodel import Field, SQLModel

from models.enums.product import ProductType, PRODUCT_TYPE_BY_ID
from models.entities.product import Product
from models.entities.supply import Supply

class ProductBase(SQLModel):
  name: str
  description: str
  price: float = 0.0
  stock: int = 0
  stock_minimum: int = 0

class ProductCreate(ProductBase):
  type_id: int = Field(default=1, description="Tipo de producto: 1. Planta 2. Insumo 3. Herramienta")
  location: str | None = Field(default=None, description="Debes ingresar el bloqueo o pasillo donde se guardó el stock")
  
  def create_dump(self):
    product = self.model_dump(exclude_none=True)
    if product.get("type") == None:
      product["type"] = PRODUCT_TYPE_BY_ID.get(self.type_id)
      product.pop("type_id")
    return product
    
class ProductUpdate(ProductBase):
  id: int | None
  name: str | None
  description: str | None
  price: float | None = 0.0
  stock: int | None = 0
  stock_minimum: int | None = 10
  location: str | None
  active: bool | None
  type_id: int | None
  created_at: str | None
  updated_at: str | None
  
class ProductRead(ProductBase):
  id: int | None
  active: bool
  type: str
  created_at: str
  updated_at: str
  location: str | None
  
  @staticmethod
  def from_db(product: Product):
    return ProductRead(
      id=product.id,
      name=product.name,
      description=product.description,
      price=product.price,
      stock=product.stock,
      stock_minimum=product.stock_minimum,
      location=product.location,
      active=product.active,
      type=product.type,
      created_at=product.created_at.isoformat(),
      updated_at=product.updated_at.isoformat()
    ) 
  
  @staticmethod
  def supply_and_product(product: Product, supply: Supply):
    return {
      "id": product.id,
      "name": product.name,
      "description": product.description,
      "type": product.type,
      "price": product.price,
      "stock": product.stock,
      "sub_type_info": {
        "sub_type": supply.type,
        "stock_minimum": product.stock_minimum,
        "unit_meausure": supply.unit_measure,
        "unit_quantity": supply.unit_quantity,
        "expiration_date": supply.expiry_date,
      },
      "location": product.location,
      "active": product.active,
      "created_at": product.created_at.isoformat(),
      "updated_at": product.updated_at.isoformat(),
    }
  
class ProductOrder(SQLModel):
  id: int
  quantity: int
  