from sqlmodel import SQLModel, Field

from models.entities.plant import Plant
from models.entities.product import Product
from models.enums.plant import Irrigation_Enum, Light_Enum, Plant_type_Enum


class PlantBase(SQLModel):
    scientific_name: str
    type_plant: Plant_type_Enum 
    required_irrigation: Irrigation_Enum
    required_light: Light_Enum
    ideal_temperature: int
    perishable: bool


class PlantCreate(PlantBase):
    scientific_name: str
    type_plant: Plant_type_Enum 
    required_irrigation: Irrigation_Enum
    required_light: Light_Enum
    ideal_temperature: int
    perishable: bool
    id_product:int

class PlantRead(PlantCreate):
    
    @staticmethod
    def ProductPlant(product: Product, plant: Plant):
        return {
      "id": product.id,
      "Name": product.name,
      "Scientific_name": plant.scientific_name,
      "Plant_type": plant.type_plant
    }

class PlantUpdate(PlantCreate):
    pass