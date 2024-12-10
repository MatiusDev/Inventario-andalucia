from fastapi import APIRouter, status

from models.schemas.tool import ToolCreate, ToolUpdate, ToolRead
from services.tool_service import SToolDependency

route = APIRouter()

@route.post("/", response_model=ToolRead)
async def create_tool(tool: ToolCreate, tool_service: SToolDependency):
    return tool_service.create(tool)

# @route.put("/{tool_id}", response_model=ToolUpdate, status_code=status.HTTP_201_CREATED)
# async def update_tool(tool_id: int, tool: ToolUpdate, tool_service: SToolDependency):
#     return tool_service.update(tool_id, tool)

# @route.get("/", response_model= list[ToolRead])
# async def list_tool(tool_service: SToolDependency):
#     return tool_service.get_all()

# @route.delete("/tool/{tool_id}")
# async def delete_tool(tool_id: int, tool_service: SToolDependency):
#     return tool_service.delete(tool_id)


# Comentarios cambios