from typing import Annotated
from fastapi import Depends, HTTPException, status
from config.db_adapter import DBSession
from sqlmodel import select

from models.entities.tool import Tool
from models.schemas.tool import ToolCreate, ToolUpdate, ToolRead

class ToolService:
    def __init__(self, db: DBSession) -> None:
        self.db = db

    def create(self, tool_data: ToolCreate):
        tool_db = Tool.model_validate(tool_data)
        self.db.add(tool_db)
        self.db.commit()
        self.db.refresh(tool_db)
        tool_read = ToolRead.model_validate(tool_db)
        return tool_read
    
    # def get_all(self):
    #     tools = self.db.exec(select(Tool)).all() or []
    #     return tools
    
    # def update(self, id: int, tool_data: ToolUpdate):
    #     tool_db = self.db.get(Tool, id)
    #     if tool_db == None:
    #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tool doesn't exist")
    #     tool_data_dict = tool_data.model_dump(exclude_unset=True)
    #     tool_db.sqlmodel_update(tool_data_dict)
    #     self.db.add(tool_db)
    #     self.db.commit()
    #     self.db.refresh(tool_db)
    #     return tool_db
    
    # def delete(self, id: int):
    #     tool_db = self.db.get(Tool, id)
    #     if tool_db == None:
    #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tool doesn't exist")
    #     self.db.delete(tool_db)
    #     self.db.commit()
    #     return {"message": "Tool deleted", "status": "success"}
    
SToolDependency = Annotated[ToolService, Depends(ToolService)]