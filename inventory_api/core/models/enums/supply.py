from enum import Enum

class TypeSupply(str, Enum):
	SEEDS = "Semillas",
	FERTILIZERS = "Fertilizantes",
	PESTICIDES = "Pesticidas",
	HERBICIDES = "Herbicidas",
	SUBSTRATES = "Sustratos"
 
TYPE_SUPPLY_BY_ID = {
	1: TypeSupply.SEEDS,
	2: TypeSupply.FERTILIZERS,
	3: TypeSupply.PESTICIDES,
	4: TypeSupply.HERBICIDES,
	5: TypeSupply.SUBSTRATES
}