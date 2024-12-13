from fastapi import APIRouter, status

from core.models.schemas.tool import ToolCreate, ToolUpdate
from core.services.tool_service import SToolDependency

route = APIRouter()

@route.post("/", status_code=201)
async def create_tool(tool: ToolCreate, tool_service: SToolDependency):
    return tool_service.create(tool)

@route.get("/", status_code=200)
def get_all_tools(tool_service: SToolDependency):
    return tool_service.get_all()

@route.get("/{id}", status_code=200)
def get_tool(id: int, tool_service: SToolDependency):
    return tool_service.get_by_id(id)

@route.put("/{id}")
async def update_tool(id: int, tool: ToolUpdate, tool_service: SToolDependency):
    return tool_service.update(id, tool)

@route.delete("/{id}")
async def delete_tool(id: int, tool_service: SToolDependency):
    return tool_service.delete(id)


# Comentarios cambios