from fastapi import APIRouter

# Importando las vistas y los routers
from controllers import product_controller

routes = APIRouter()

routes.include_router(product_controller.route, tags=["Products"], prefix="/products")