from enum import Enum


class Type_Supply(str, Enum):
    SEEDS = "Semillas",
    FERTILIZERS = "Fertilizantes",
    PESTICIDES = "Pesticidas",
    HERBICIDES = "Herbicidas",
    SUBSTRATES = "Sustratos"

TYPE_SUPPLY_BY_ID = {
    1: Type_Supply.SEEDS,
    2: Type_Supply.FERTILIZERS,
    3: Type_Supply.PESTICIDES,
    4: Type_Supply.HERBICIDES,
    5: Type_Supply.SUBSTRATES
}