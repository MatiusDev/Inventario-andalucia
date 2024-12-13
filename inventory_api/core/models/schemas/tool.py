from sqlmodel import SQLModel

from core.models.entities.tool import Tool
from core.models.enums.tool import Category_Enum, Maintenance_Enum, CATEGORY_BY_ID, MAINTENANCE_BY_ID

class ToolBase(SQLModel):
    brand: str
    
    

class ToolRead(ToolBase):
    id: int | None
    category: str
    brand: str
    type_maintenance: str
    product_id: int

    @staticmethod
    def from_db(tool: Tool):
        return ToolRead(
            id = tool.id,
            category=tool.category,
            brand = tool.brand,
            type_maintenance=tool.type_maintenance,
            product_id=tool.product_id
        )

class ToolCreate(ToolBase):
    category: int
    type_maintenance: int

    def create_dump(self):
        category = Category_Enum(CATEGORY_BY_ID.get(self.category)).value
        maintenance = Maintenance_Enum(MAINTENANCE_BY_ID.get(self.type_maintenance)).value

        self.category = None
        self.type_maintenance = None
        tool = self.model_dump(exclude_none=True)
        return{
            **tool,
            "category" : category,
            "type_maintenance" : maintenance
        }

class ToolUpdate(ToolBase):
    category: int | None
    brand: str | None
    type_maintenance: int | None

    def update_dump(self):
        if self.brand == "":
            self.brand = None

        category = None
        maintenance = None

        if self.category != None:
            if(isinstance(self.category, int)) and 0 > self.category > len(CATEGORY_BY_ID):
                category = Category_Enum(CATEGORY_BY_ID.get(self.category)).value
        
        if self.type_maintenance != None:
            if(isinstance(self.type_maintenance, int)) and 0 > self.type_maintenance > len(MAINTENANCE_BY_ID):
                maintenance = Maintenance_Enum(MAINTENANCE_BY_ID.get(self.type_maintenance)).value
        
        tool = self.model_dump(exclude_none=True)

        if category != None:
            tool["category"] = category
        if maintenance != None:
            tool["type_maintenance"] = maintenance
        
        return tool