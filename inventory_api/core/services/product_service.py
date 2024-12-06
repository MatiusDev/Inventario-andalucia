from typing import Annotated
from fastapi import Depends, HTTPException

from config.db_adapter import DBSession

from sqlmodel import select

from models.entities.plant import Plant
from models.schemas.plant import PlantCreate, PlantRead
from models.entities.product import Product
from models.entities.supply import Supply
from models.schemas.product import ProductCreate, ProductRead

class ProductService:
  def __init__(self, db: DBSession) -> None:
    self.db = db
  
  def get_all(self):
    products_db = self.db.exec(select(Product)).all() or []
    return products_db
  
  async def get_all_supplies(self):
    products_db = self.db.exec(select(Product, Supply).join(Supply)).all()
    
    # List Comprehesion
    products = [ProductRead.supply_and_product(product, supply) for product, supply in products_db]
    
    products_sup = []
    for product, supply in products_db:
      products_sup.append(ProductRead.supply_and_product(product, supply))
    # products = [{"product": product, "supply": supply } for product, supply in products_db]
    return products_sup
  
  async def get_all_plants(self):
    products_db = self.db.exec(select(Product, Plant).join(Plant)).all()
    
    # List Comprehesion
    products = [PlantRead.ProductPlant(product, plant) for product, plant in products_db]
        
    return products


  def get_by_id(self, id: int):
    product = self.db.get(Product, id)
    
    if product == None:
      raise HTTPException(status_code=404, detail="Product not found")
    return ProductRead(id=product.id, name=product.name, price=product.price)

  def create(self, product: ProductCreate):
    product_db = Product.model_validate(product.model_dump())
    self.db.add(product_db)
    self.db.commit()
    self.db.refresh(product_db)
    
    product_read = ProductRead.model_validate(product_db)
    return product_read

    # if product.type_product == "Plantas":
    #   plant_data = PlantCreate()


  # def update_product(self, id: int, product: ProductCreate):
  #   product_db = self.db.get(Product, id)

  #   if product_db == None:
  #     raise HTTPException(status_code=404, detail="Product not found")
    
  #   product_db.name = product.name
  #   product_db.price = product.price
  #   self.db.add(product_db)
  #   self.db.commit()
  #   self.db.refresh(product_db)
  #   return ProductRead(id=product_db.id, name=product_db.name, price=product_db.price)

  # def delete_product(self, id: int):
  #   product = self.db.get(Product, id)
    
  #   if product == None:
  #     raise HTTPException(status_code=404, detail="Product not found")
    
  #   self.db.delete(product)
  #   self.db.commit()
  #   return {"message": "Product deleted", "status": "success"}
  
SProductDependency = Annotated[ProductService, Depends(ProductService)]
    