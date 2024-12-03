from fastapi import APIRouter, status

from models.entities.tool import Tool
from models.schemas.tool import ToolCreate, ToolUpdate
from services.tool_service import SToolDependency

route = APIRouter()

@route.post("/", response_model=Tool)
async def create_tool(
    tool: ToolCreate,
    tool_service: SToolDependency
    ):
    return tool_service.newTool(tool)

@route.put("/{tool_id}", response_model=Tool, status_code=status.HTTP_201_CREATED)
async def update_tool(tool_id: int, tool: ToolUpdate, tool_service: SToolDependency):
    return tool_service.update_tool(tool_id, tool)

@route.get("/", response_model= list[Tool])
async def list_tool(tool_service: SToolDependency):
    return tool_service.list_plant()

@route.delete("/tool/{tool_id}")
async def delete_tool(tool_id: int, tool_service: SToolDependency):
    return tool_service.delete_tool(tool_id)