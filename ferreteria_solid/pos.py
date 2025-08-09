# ferreteria_solid/pos.py
from abc import ABC, abstractmethod

class Descuento(ABC):
    """Interfaz (clase base abstracta) para una estrategia de descuento. Abierta a extensión."""
    @abstractmethod
    def calcular(self, total: float) -> float:
        pass

class DescuentoPorcentaje(Descuento):
    """Implementación para descuento por porcentaje."""
    def __init__(self, porcentaje: float):
        self.porcentaje = porcentaje

    def calcular(self, total: float) -> float:
        return total * (self.porcentaje / 100)

class DescuentoMontoFijo(Descuento):
    """Implementación para descuento de monto fijo."""
    def __init__(self, monto: float):
        self.monto = monto

    def calcular(self, total: float) -> float:
        return self.monto

class Venta:
    """Clase Venta. Cerrada a modificación, pero abierta a extensión a través de la interfaz Descuento."""
    def __init__(self, total: float):
        self.total = total
        self.descuentos = []

    def agregar_descuento(self, descuento: Descuento):
        self.descuentos.append(descuento)

    def calcular_total_final(self) -> float:
        total_descuento = 0
        for descuento in self.descuentos:
            total_descuento += descuento.calcular(self.total)
        return self.total - total_descuento
