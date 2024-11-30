from fastapi import APIRouter, Depends

# Importando las vistas y los routers
from controllers.auth_controller import route as auth_route
from controllers.role_controller import route as role_route
from controllers.product_controller import route as product_route

routes = APIRouter()

routes.include_router(auth_route, tags=["Auth"], prefix="/auth")
routes.include_router(product_route, tags=["Products"], prefix="/products")
routes.include_router(role_route, tags=["Roles"], prefix="/roles")