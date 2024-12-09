from enum import Enum


class Type_Supply(str, Enum):
    SEMILLAS = "Semillas",
    FERTILIZANTES = "Fertilizantes",
    PESTICIDAS = "Pesticidas",
    HERBICIDAS = "Herbicidas",
    SUSTRATOS = "Sustratos"