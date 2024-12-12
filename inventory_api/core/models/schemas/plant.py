from enum import Enum
from sqlmodel import SQLModel, Field

class typePlant_Enum(str, Enum):
    EXTERIOR = "exterior"
    INTERIOR = "interior"
    MEDICINAL = "medicinal"
    DECORATIVE = "decorativa"

class requiredWatering_Enum(str, Enum):
    DIALY = "diario"
    WEEKLY = "semanal"
    MONTHLY = "mensual"

class requiredLight_Enum(str, Enum):
    SHADOW = "sombra"
    HALF_SHADE = "media sombra"
    FULL_SUN = "pleno sol"

class yes_no_Enum(str, Enum):
    YES = "Si"
    NO = "No"

class PlantBase(SQLModel):
    id_product: int = Field(foreign_key="product.id")
    name_scientific: str = Field(default=None)
    type_plant: typePlant_Enum = Field(default=typePlant_Enum.EXTERIOR)
    required_watering: requiredWatering_Enum = Field(default=requiredWatering_Enum.DIALY)
    required_light: requiredLight_Enum = Field(default=requiredLight_Enum.SHADOW)
    ideal_temperature: int = Field(default=None)
    life_time: yes_no_Enum = Field(default=yes_no_Enum.YES)

class PlantCreate(PlantBase):
    pass

class PlantUpdate(PlantBase):
    pass