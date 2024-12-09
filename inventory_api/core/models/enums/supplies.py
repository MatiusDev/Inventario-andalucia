from enum import Enum

class TypeSupply(str, Enum):
	SEEDS = "Semillas",
	FERTILIZERS = "Fertilizantes",
	PESTICIDES = "Pesticidas",
	HERBICIDES = "Herbicidas",
	SUBSTRATES = "Sustratos"