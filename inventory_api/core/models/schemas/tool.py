from enum import Enum
from sqlmodel import SQLModel, Field

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

class ToolBase(SQLModel):
    id_product: int = Field(foreign_key="product.id")
    category: CategoryEnum = Field(default=CategoryEnum.APERO)
    material: MaterialEnum = Field(default=MaterialEnum.METAL)
    brand: str = Field(default=None)
    type_maintenance: TypeMaintenance_Enum = Field(default=TypeMaintenance_Enum.CORRECTIVO)

class ToolCreate(ToolBase):
    pass

class ToolUpdate(ToolBase):
    pass