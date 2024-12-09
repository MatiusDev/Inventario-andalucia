from enum import Enum

class Type_Product(str, Enum):
    PLANT = "Planta"
    SUPPLY = "Insumo"
    TOOL = "Herramienta"

TYPE_PRODUCT_BY_ID = {
    1: Type_Product.PLANT,
    2: Type_Product.SUPPLY,
    3: Type_Product.TOOL
}