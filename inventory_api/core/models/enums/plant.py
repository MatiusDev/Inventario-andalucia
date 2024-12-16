from enum import Enum

class Plant_type_Enum(str, Enum):
    INTERIOR = "Interior"
    EXTERIOR = "Exterior"
    MEDICINAL = "Medicinal"
    ORNAMENTAL = "Decorativo"

PLANT_TYPE_BY_ID = {
    1: Plant_type_Enum.INTERIOR,
    2: Plant_type_Enum.EXTERIOR,
    3: Plant_type_Enum.MEDICINAL,
    4: Plant_type_Enum.ORNAMENTAL 
}

class Irrigation_Enum(str, Enum):
    DAILY = "Diario"
    WEEKLY = "Semanal"
    MONTLY = "Mensual"

IRRIGATION_BY_ID = {
    1: Irrigation_Enum.DAILY,
    2: Irrigation_Enum.WEEKLY,
    3: Irrigation_Enum.MONTLY,
}

class Light_Enum(str, Enum):
    SHADE = "Sombra"
    HALF_SHADE = "Media sombra"
    FULL_SUN = "Pleno sol"

LIGHT_BY_ID = {
    1: Light_Enum.SHADE,
    2: Light_Enum.HALF_SHADE,
    3: Light_Enum.FULL_SUN,
}