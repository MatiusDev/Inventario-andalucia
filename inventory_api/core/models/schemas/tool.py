from enum import Enum
from sqlmodel import SQLModel

class CategoryEnum(str, Enum):
    APERO = "Aperos"
    MAQUINAS = "Máquinas"

class MaterialEnum(str, Enum):
    METAL = "Metal"
    MADERA = "Madera"
    PLASTICO = "Plástico"

class TypeMaintenance_Enum(str, Enum):
    CORRECTIVO = "Correctivo"
    PREVENTIVO = "Preventivo"
    PREDICTIVO = "Predictivo"

# DTO
class ToolBase(SQLModel):
    category: str
    material: str
    brand: str
    type_maintenance: str
    id_product: int

class ToolRead(ToolBase):
    id: int | None

class ToolCreate(ToolBase):
    pass

class ToolUpdate(ToolBase):
    pass