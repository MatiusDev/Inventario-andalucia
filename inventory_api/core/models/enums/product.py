from enum import Enum

class ProductType(str, Enum):
    PLANT = "Planta"
    SUPPLY = "Insumo"
    TOOL = "Herramienta"
    
PRODUCT_TYPE_BY_ID = {
  1: ProductType.PLANT,
  2: ProductType.SUPPLY,
  3: ProductType.TOOL
}
