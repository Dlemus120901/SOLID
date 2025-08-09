# ferreteria_solid/proveedores.py
from abc import ABC, abstractmethod

class Proveedor(ABC):
    """Clase base para proveedores. Cualquier subclase debe poder sustituirla."""
    def __init__(self, nombre: str):
        self.nombre = nombre

    @abstractmethod
    def procesar_orden_compra(self):
        pass

class ProveedorLocal(Proveedor):
    """Subclase para proveedor local."""
    def procesar_orden_compra(self):
        
        print(f"✅ [LSP] Procesando orden de compra para proveedor local: {self.nombre} (envío estándar).")

class ProveedorInternacional(Proveedor):
    """Subclase para proveedor internacional."""
    def procesar_orden_compra(self):
        print(f"✅ [LSP] Procesando orden para proveedor internacional: {self.nombre} (incluye trámites de aduana).")
