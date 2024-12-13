from typing import Annotated
from fastapi import Depends, HTTPException
from sqlmodel import select

from core.config.db_adapter import DBSession

from core.models.entities.product import Product
from core.models.entities.tool import Tool
from core.models.schemas.tool import ToolCreate, ToolUpdate, ToolRead
from core.models.enums.product import ProductType

class ToolService:
    def __init__(self, db: DBSession) -> None:
        self.db = db

    def create(self, product_id: int, tool_data: ToolCreate):
        try:
            product_db = self.db.get(Product, product_id)
        
            if product_db is None:
                return {
					"status_code": 404,
					"detail": "El producto no existe",
					"status": "fail",
				}
            
            if product_db.type != ProductType.TOOL.value:
                return {
					"status_code": 400,
					"detail": f"Este producto no es una herramienta, debes agregarlo en {product_db.type}",
					"status": "fail",
				}
            
            tool_db = Tool.model_validate(tool_data.create_dump())
            tool_db.product_id = product_id

            self.db.add(tool_db)
            self.db.commit()
            self.db.refresh(tool_db)

            tool_read = ToolRead.from_db(tool_db)
            return  { "data": tool_read, "status": "success" }
        
        except Exception as err:
            self.db.rollback()
            return { "status_code": 500, "detail": str(err), "status": "error" }
    
    
    def get_all(self):
        tools_db = self.db.exec(select(Tool)).all() or []
        return { "data" : tools_db, "status": "success" }
    
    def get_by_id(self, id:int):
        tool = self.db.get(Tool, id)

        if tool is None:
            return { "status_code": 404, "detail": "Herramienta no encontrada", "status": "fail" }
        
        read_tool = ToolRead.from_db(tool)        
        return { "data": read_tool, "status": "success" }
    
    def update(self, id: int, tool: ToolUpdate):
        try:
            tool_db = self.db.get(Tool, id)
            
            if tool_db is None:
                return { "status_code": 404, "detail": "Herramienta no encontrada", "status": "fail" }
            
            tool_db.sqlmodel_update(tool.update_dump())

            self.db.add(tool_db)
            self.db.commit()
            self.db.refresh(tool_db)

            tool_read = ToolRead.from_db(tool_db)
            return { "data": tool_read, "status": "success" }
        

        except Exception as err:
            self.db.rollback()
            return { "status_code": 500, "detail": str(err), "status": "error" }
        

    def delete(self, id: int):
        try:
            tool_db = self.db.get(Tool, id)
            
            if tool_db is None:
                return { "status_code": 404, "detail": "Herramienta no encontrada", "status": "fail" }
            
            self.db.delete(tool_db)
            self.db.commit()
            
            return {"message": "Tool deleted", "status": "success"}
        except Exception as err:
            self.db.rollback()
            return { "status_code": 500, "detail": str(err), "status": "error" }
        

SToolDependency = Annotated[ToolService, Depends(ToolService)]