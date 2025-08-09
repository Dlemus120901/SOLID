# ferreteria_solid/reportes.py
from abc import ABC, abstractmethod

class FuenteDatos(ABC):
    """Abstracción de la que dependen tanto los módulos de alto como de bajo nivel."""
    @abstractmethod
    def obtener_datos(self) -> list:
        pass

class BaseDatosVentas(FuenteDatos):
    """Módulo de bajo nivel: detalle de implementación."""
    def obtener_datos(self) -> list:
        print("...Obteniendo datos desde la base de datos PostgreSQL...")
        return [{"id": 1, "total": 150.75}, {"id": 2, "total": 200.00}]

class ArchivoCsvVentas(FuenteDatos):
    """Otro módulo de bajo nivel: detalle de implementación."""
    def obtener_datos(self) -> list:
        print("...Obteniendo datos desde un archivo report.csv...")
        return [{"id": 101, "total": 88.20}, {"id": 102, "total": 45.30}]

class GeneradorReportes:
    """Módulo de alto nivel. Depende de la abstracción FuenteDatos, no de una implementación concreta."""
    def __init__(self, fuente: FuenteDatos):
        self.fuente = fuente

    def generar_reporte_ventas(self):
        print(f"✅ [DIP] Generando reporte con datos de '{self.fuente.__class__.__name__}'")
        datos = self.fuente.obtener_datos()
        # Lógica para formatear y presentar el reporte
        for venta in datos:
            print(f"   - Venta ID: {venta['id']}, Total: ${venta['total']:.2f}")
