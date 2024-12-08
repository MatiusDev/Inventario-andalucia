from fastapi import APIRouter, Depends

# Importando las vistas y los routers
from controllers.auth_controller import route as auth_route
from controllers.user_controller import route as user_route
from controllers.role_controller import route as role_route
from controllers.supplier_controller import route as supplier_route
from controllers.order_controller import route as order_route
from controllers.product_controller import route as product_route
from controllers.tool_controller import route as tool_route
from controllers.plant_controller import route as plant_route
from controllers.supply_controller import route as supply_route
from controllers.notify_controller import route as notify_route

routes = APIRouter()

routes.include_router(auth_route, tags=["Auth"], prefix="/auth")
routes.include_router(product_route, tags=["Products"], prefix="/products")
routes.include_router(tool_route, tags=["Tools"], prefix="/tools")
routes.include_router(plant_route, tags=["Plants"], prefix="/plants")
routes.include_router(supply_route, tags=["Supplies"], prefix="/supplies")
routes.include_router(role_route, tags=["Roles"], prefix="/roles")
routes.include_router(notify_route, tags=["Notifications"], prefix="/notifications")
routes.include_router(user_route, tags=["Users"], prefix="/users")
routes.include_router(role_route, tags=["Roles"], prefix="/roles")
routes.include_router(order_route, tags=["Orders"], prefix="/orders")
routes.include_router(supplier_route, tags=["Suppliers"], prefix="/suppliers")
routes.include_router(product_route, tags=["Products"], prefix="/products")
