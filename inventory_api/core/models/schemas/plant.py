from sqlmodel import SQLModel, Field

from models.entities.plant import Plant
from models.entities.product import Product
from models.enums.plant import Irrigation_Enum, Light_Enum, Plant_type_Enum, PLANT_TYPE_BY_ID, LIGHT_BY_ID, IRRIGATION_BY_ID


class PlantBase(SQLModel):
    scientific_name: str
    ideal_temperature: int
   
class PlantCreate(PlantBase):
    type_id: int
    required_irrigation_id: int
    required_light_id: int
    
    def create_dump(self):
        plant_type = Plant_type_Enum(PLANT_TYPE_BY_ID.get(self.type_id)).value
        irrigation = Irrigation_Enum(IRRIGATION_BY_ID.get(self.required_irrigation_id)).value
        light = Light_Enum(LIGHT_BY_ID.get(self.required_light_id)).value
        self.type_id = None
        self.required_irrigation_id = None
        self.required_light_id = None
        
        plant = self.model_dump(exclude_none=True)
        return{
            **plant,
            "type": plant_type,
            "required_irrigation": irrigation,
            "required_light": light
        }

class PlantRead(PlantBase):
    id: int | None
    type: str
    required_irrigation: str
    required_light: str
    product_id: int

    @staticmethod
    def from_db(plant: Plant):
        return PlantRead (
            id = plant.id,
            product_id=plant.product_id,
            scientific_name=plant.scientific_name,
            type = plant.type,
            required_irrigation=plant.required_irrigation,
            required_light=plant.required_light,
            ideal_temperature=plant.ideal_temperature
        )

class PlantUpdate(PlantBase):
    scientific_name: str | None
    ideal_temperature: int | None
    type_id = int | None
    required_irrigation_id: int | None
    required_light_id: int | None

    def update_dump(self):
        if self.scientific_name == "":
            self.scientific_name = None
        if self.ideal_temperature == "":
            self.ideal_temperature = None
        
        plant_type = None
        irrigation = None
        light = None

        if self.type_id != None:
            if (isinstance(self.type_id, int)) and 0 > self.type_id > len(PLANT_TYPE_BY_ID):
                plant_type = Plant_type_Enum(PLANT_TYPE_BY_ID.get(self.type_id)).value
        
        if self.required_irrigation_id != None:
            if (isinstance(self.required_irrigation_id, int)) and 0 > self.required_irrigation_id > len(IRRIGATION_BY_ID):
                irrigation = Irrigation_Enum(IRRIGATION_BY_ID.get(self.required_irrigation_id)).value
        
        if self.required_light_id != None:
            if (isinstance(self.required_light_id, int)) and 0 > self.required_light_id > len(IRRIGATION_BY_ID):
                light = Light_Enum(LIGHT_BY_ID.get(self.required_light_id)).value

        plant = self.model_dump(exclude_none=True)
        
        if plant_type != None:
            plant["type"] = plant_type
        if irrigation != None:
            plant["required_irrigation"] = irrigation
        if irrigation != None:
            plant["required_light"] = light

        return plant
