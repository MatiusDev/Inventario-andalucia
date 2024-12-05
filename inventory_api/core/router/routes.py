from fastapi import APIRouter, Depends

# Importando las vistas y los routers
from controllers.auth_controller import route as auth_route
from controllers.role_controller import route as role_route
from controllers.product_controller import route as product_route
from controllers.tool_controller import route as tool_route
# from controllers.plant_controller import route as plant_route
from controllers.supply_controller import route as supply_route

routes = APIRouter()

routes.include_router(auth_route, tags=["Auth"], prefix="/auth")
routes.include_router(product_route, tags=["Products"], prefix="/products")
routes.include_router(tool_route, tags=["Tools"], prefix="/tools")
# routes.include_router(plant_route, tags=["Plants"], prefix="/plants")
routes.include_router(supply_route, tags=["Supplies"], prefix="/supplies")
routes.include_router(role_route, tags=["Roles"], prefix="/roles")