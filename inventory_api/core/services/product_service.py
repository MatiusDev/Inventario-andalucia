from typing import Annotated
from fastapi import Depends, HTTPException

from config.db_adapter import DBSession

from sqlmodel import select

from models.entities.product import Product
from models.schemas.product import ProductCreate, ProductRead

class ProductService:
  def __init__(self, db: DBSession) -> None:
    self.db = db
  
  def get_all_products(self):
    products = self.db.exec(select(Product)).all() or []
    return products
  
  def get_product_by_id(self, id: int):
    product = self.db.get(Product, id)
    
    if product == None:
      raise HTTPException(status_code=404, detail="Product not found")
    return ProductRead(id=product.id, name=product.name, price=product.price)

  def new_product(self, product: ProductCreate):
    new_product = Product(name=product.name, price=product.price)
    # Agrega un nuevo producto a la base de datos
    self.db.add(new_product)
    # Realiza los cambios en la base de datos
    self.db.commit()
    # Realiza los cambios en el objeto (Referencia al producto de la BD, así obtiene el nuevo ID)
    self.db.refresh(new_product)
    return ProductRead(id=new_product.id, name=new_product.name, price=new_product.price)

  def update_product(self, id: int, product: ProductCreate):
    product_db = self.db.get(Product, id)

    if product_db == None:
      raise HTTPException(status_code=404, detail="Product not found")
    
    product_db.name = product.name
    product_db.price = product.price
    self.db.add(product_db)
    self.db.commit()
    self.db.refresh(product_db)
    return ProductRead(id=product_db.id, name=product_db.name, price=product_db.price)

  def delete_product(self, id: int):
    product = self.db.get(Product, id)
    
    if product == None:
      raise HTTPException(status_code=404, detail="Product not found")
    
    self.db.delete(product)
    self.db.commit()
    return {"message": "Product deleted", "status": "success"}

  def get_products(self, products: list[ProductCreate]):
    product_ids = [product.id for product in products]
    products_db = self.db.exec(select(Product).where(Product.id.in_(product_ids))).all()
    
    # Validando que la consulta si tenga la misma cantidad de productos id
    product_db_ids = [product.id for product in products_db]
    response = self.validate_products(product_ids, product_db_ids)
    
    if response["status"] != "success":
      return response
    return { "data": products_db, "status": "success" }
  
  def validate_products(self, product_ids: list, product_db_ids: list):
    product_ids_set = set(product_ids)
    product_db_ids_set = set(product_db_ids)
    if len(product_ids) != len(product_db_ids):
      products_not_found = product_ids_set - product_db_ids_set
      return { 
        "status_code": 404,
        "detail": f"Los siguientes ids de producto no se encontraron: {products_not_found}", 
        "status": "fail"
      }
    return { "status": "success" }


SProductDependency = Annotated[ProductService, Depends(ProductService)]
    