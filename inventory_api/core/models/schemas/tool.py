from enum import Enum
from typing import Any
from sqlmodel import SQLModel

# DTO
class ToolBase(SQLModel):
    category: str
    material: str
    brand: str
    type_maintenance: str
    id_product: int

class ToolRead(SQLModel):
    id: Any | None
    category: str
    material: str
    brand: str
    type_maintenance: str
    id_product: int

class ToolCreate(ToolBase):
    pass

class ToolUpdate(ToolBase):
    pass