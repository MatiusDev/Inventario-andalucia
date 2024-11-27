from fastapi import APIRouter

# Importando las vistas y los routers
from controllers.product_controller import route as product_route
# from controllers.auth_controller import route as auth_route

routes = APIRouter()

routes.include_router(product_route, tags=["Products"], prefix="/products")
# routes.include_router(auth_route, tags=["Auth"], prefix="/auth")