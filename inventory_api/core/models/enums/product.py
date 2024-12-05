from enum import Enum

class Type_Product(Enum):
    PLANT = "Planta"
    SUPPLY = "Insumo"
    TOOL = "Herramienta"

class State_Enum(Enum):
    AVAILABLE = "Disponible"
    PENDING = "Pendiente"
    SPENT = "Agotado"