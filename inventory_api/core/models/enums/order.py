from enum import Enum

class Status(str, Enum):
  PROCESSED = "Procesado"
  PENDING = "Pendiente"
  CANCELED = "Cancelado"
  
class OrderType(str, Enum):
  USER = "Salida"
  SUPPLIER = "Entrada"
  
ORDER_TYPE_BY_ID = {
  1: OrderType.USER,
  2: OrderType.SUPPLIER
}