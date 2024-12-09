from typing import Annotated
from fastapi import Depends, HTTPException, status
from config.db_adapter import DBSession
from sqlmodel import select

from models.entities.product import Product
from models.entities.tool import Tool
from models.schemas.tool import ToolCreate, ToolUpdate, ToolRead
from models.enums.type_Product import Type_Product

class ToolService:
    def __init__(self, db: DBSession) -> None:
        self.db = db

    def create(self, tool_data: ToolCreate):
        tool_db = Tool.model_validate(tool_data)
        product_db = self.db.get(Product, tool_data.id_product)
        if product_db is None:
            raise HTTPException(status_code=404, detail="El producto no existe")
    
        if product_db.type_product != Type_Product.HERRAMIENTA.value:
            raise HTTPException(status_code=400, detail="No puedes agregar este tipo de producto en herramientas")

        self.db.add(tool_db)
        self.db.commit()
        self.db.refresh(tool_db)
        tool_read = ToolRead.model_validate(tool_db)
        return tool_read
    
    def get_all(self):
        tools_db = self.db.exec(select(Tool)).all() or []
        return tools_db
    
    def get_by_id(self, id:int):
        tool = self.db.get(Tool, id)

        if tool is None:
            raise HTTPException(status_code=404, detail="Tool not found")
        
        return ToolRead(**vars(tool))
    
    def update(self, id: int, tool: ToolUpdate):
        tool_db = self.db.get(Tool, id)
        product_db = self.db.get(Product, tool.id_product)
        if product_db is None:
            raise HTTPException(status_code=404, detail="Product doesn't exist")
        
        if product_db.type != Type_Product.TOOL:
            raise HTTPException(status_code=400, detail="No puedes agregar este tipo de producto en herramientas")

        if tool_db is None:
            raise HTTPException(status_code=404, detail="Tool doesn't exist")
        
        for attr, value in tool.model_dump(exclude_unset=True).items():
            setattr(tool_db, attr, value)

        self.db.add(tool_db)
        self.db.commit()
        self.db.refresh(tool_db)
        return ToolRead(
            id=tool_db.id,
            **tool.model_dump(exclude_unset=True)
        )
    
    def delete(self, id: int):
        tool = self.db.get(Tool, id)
        
        if tool is None:
            raise HTTPException(status_code=404, detail="Tool doesn't exist")
        
        self.db.delete(tool)
        self.db.commit()
        return {"message": "Tool deleted", "status": "success"}
    
SToolDependency = Annotated[ToolService, Depends(ToolService)]