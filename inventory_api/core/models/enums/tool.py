from enum import Enum

class Category_Enum(str, Enum):
    MANUAL = "Manual";
    SEMIMANUAL = "Semimanual"
    AUTOMATIC = "Automatica"

CATEGORY_BY_ID = {
    1: Category_Enum.MANUAL,
    2: Category_Enum.SEMIMANUAL,
    3: Category_Enum.AUTOMATIC,
}


class Maintenance_Enum(str, Enum):
    CLEANING = "Limpieza",
    SHARPEN = "Afilado"

MAINTENANCE_BY_ID = {
    1: Maintenance_Enum.CLEANING,
    2: Maintenance_Enum.SHARPEN
}