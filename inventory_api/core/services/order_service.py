from typing import Annotated, List
from fastapi import Depends
# Dependencias
from config.db_adapter import DBSession
from config.auth_token import UserDependency
from services.product_service import SProductDependency

from sqlmodel import select
# Entidades y esquemas
from models.entities.order import Order
from models.entities.order_product import OrderProduct
from models.entities.product import Product
from models.entities.user import User
from models.entities.supplier import Supplier

from models.schemas.order import OrderBase, OrderCreate, OrderRead

class OrderService:
  def __init__(self, db: DBSession, user: UserDependency, product: SProductDependency) -> None:
    self.db = db
    self.user = user
    self.product = product
    
  async def get_all(self):
    orders_db = self.db.exec(select(Order, User).join(User)).all()
    
    print("HEREEEEEEEEEEE", orders_db)
    for order, user in orders_db:
      print(order, user)
      for product in order.products:
        print(product)
      
      print("HEEEEEEEEEEEEEEEEEEERE PROVEEDOR", order.suppliers)
      if order.suppliers:
        for supplier in order.suppliers:
          print(supplier)
    
    return { "data" : "Reading orders", "status": "success" }
  
  async def get_by_id(self, id: int):
    order = self.db.get(Order, id)
    
    if order == None:
      return { "status_code": 404, "detail": "Order not found", "status": "fail" }
    
    read_order = OrderRead.model_validate(order)
    return { "data": read_order, "status": "success"}
  
  async def create(self, order: OrderCreate):
    if (order.id_supplier == 0 or
      order.id_supplier <= -2):
      return { "status_code": 400, "detail": "No se ha enviado un proveedor válido", "status": "fail"}
    
    # De momento se hará con una consulta directa a la DB de otras entidades.
    # Sin embargo, debe haber una consulta es desde el servicio, supplier_service o user_service para separar las responsabilidades, tomar de ejemplo la linea de consulta de productos
    if order.id_supplier != -1:
      # Creando una orden de proveedores
      supplier = self.db.get(Supplier, order.id_supplier)
      
      if supplier == None:
        return { "status_code": 404, "detail": "No se ha encontrado el proveedor", "status": "fail" }
      
      response = self.product.get_products(order.products)
      
      if response["status"] != "success":
        return response
      
      products = response["data"]
      response = self.create_supplier_order(order, products, supplier)
      
      if response["status"] != "success":
        return response
    else:     
      response = self.product.get_products(order.products)
      if response["status"] != "success":
        return response
      
      products = response["data"]
      response = self.create_user_order(order, products)
      
      if response["status"] != "success":
        return response
      
    return { "message": "Orden creada correctamente", "status": "success" }
        
  def create_user_order(self, order: OrderCreate, products_db: List[Product]):
    try:
      products = order.products
      order_db = Order.model_validate(order.create_dump())
      # Creando un arreglo de objetos clave valor "id_product" : "cantidad"
      products_quantity = { product.id : product.quantity for product in products }
      # Creando un arreglo de productos_orden mapeando cada producto y agregando la cantidad
      # Usando el valor obtenido del arreglo products_quantity
      products_db_mapped = [
        OrderProduct(
          order=order_db,
          product=product,
          quantity=products_quantity[product.id]
        ) for product in products_db]
      order_db.products.extend(products_db_mapped)
      order_db.id_user = self.user.id
      
      self.db.add(order_db)
      self.db.commit()
      self.db.refresh(order_db)
            
      return { "data": order_db, "status": "success" }
    except Exception as err:
      return { "status_code": 500, "detail": str(err), "status": "error" }
  
  def create_supplier_order(self, order: OrderCreate, products_db: List[Product], supplier: Supplier):
    try:
      products = order.products
      order_db = Order.model_validate(order.create_dump())
      # Creando un arreglo de objetos clave valor "id_product" : "cantidad"
      products_quantity = { product.id : product.quantity for product in products }
      # Creando un arreglo de productos_orden mapeando cada producto y agregando la cantidad
      # Usando el valor obtenido del arreglo products_quantity
      products_db_mapped = [
        OrderProduct(
          order=order_db,
          product=product,
          quantity=products_quantity[product.id]
        ) for product in products_db]
      order_db.products.extend(products_db_mapped)
      order_db.id_user = self.user.id
      order_db.suppliers.append(supplier)
      
      self.db.add(order_db)
      self.db.commit()
      self.db.refresh(order_db)
            
      return { "data": order_db, "status": "success" }
    except Exception as err:
      return { "status_code": 500, "detail": str(err), "status": "error" }
  
  #(2 Peticiones diferentes) Agregar o retirar productos de un orden pendiente
  #(2 Peticiones diferentes) Completar o cancelar una orden
  
  async def process_order(self, id: int):
    pass
  
  async def update(self, id: int, order: OrderBase):
    pass
  
  async def delete(self, id: int):
    pass
  
SOrderDependency = Annotated[OrderService, Depends(OrderService)]