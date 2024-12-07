from enum import Enum

class Status(str, Enum):
  PROCESSED = "Procesado"
  PENDING = "Pendiente"
  REJECTED = "Rechazado"
  
class OrderType(str, Enum):
  USER = "Salida"
  SUPPLIER = "Entrada"