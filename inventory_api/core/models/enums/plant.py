from enum import Enum

class Plant_type_Enum(str, Enum):
    INTERIOR = "Interior"
    EXTERIOR = "Exterior"
    MEDICINAL = "Medicinal"
    ORNAMENTAL = "Decorativo"


class Irrigation_Enum(str, Enum):
    DAILY = "Diario"
    WEEKLY = "Semanal"
    MONTLY = "Mensual"

class Light_Enum(str, Enum):
    SHADE = "Sombra"
    HALF_SHADE = "Media sombra"
    FULL_SUN = "Pleno sol"