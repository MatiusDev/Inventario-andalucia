from fastapi import APIRouter, status

from core.models.schemas.tool import ToolCreate, ToolUpdate
from core.services.tool_service import SToolDependency
from core.utils.response_handler import response_handler

route = APIRouter()

@route.post("/{product_id}", status_code=201)
async def create_tool(product_id: int, tool : ToolCreate, tool_service: SToolDependency):
    return await response_handler(tool_service.create(product_id,tool))

@route.get("/", status_code=200)
async def get_all_tools(tool_service: SToolDependency):
    return await response_handler(tool_service.get_all())

@route.get("/{id}", status_code=200)
async def get_tool(id: int, tool_service: SToolDependency):
    return await response_handler(tool_service.get_by_id(id))

@route.put("/{id}")
async def update_tool(id: int, tool: ToolUpdate, tool_service: SToolDependency):
    return await response_handler(tool_service.update(id, tool))

@route.delete("/{id}")
async def delete_tool(id: int, tool_service: SToolDependency):
    return await response_handler(tool_service.delete(id))

