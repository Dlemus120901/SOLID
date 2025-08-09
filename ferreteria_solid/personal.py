# ferreteria_solid/personal.py
from abc import ABC, abstractmethod

# --- Interfaces Segregadas ---
class InterfazAutenticacion(ABC):
    @abstractmethod
    def login(self): pass

class InterfazCajero(ABC):
    @abstractmethod
    def realizar_cobro(self): pass

class InterfazGestionInventario(ABC):
    @abstractmethod
    def registrar_entrada_producto(self): pass

# --- Clases que implementan solo las interfaces que necesitan ---
class Cajero(InterfazAutenticacion, InterfazCajero):
    def login(self):
        print("✅ [ISP] Cajero ha iniciado sesión.")
    
    def realizar_cobro(self):
        print("✅ [ISP] Cajero está realizando un cobro.")

class GerenteInventario(InterfazAutenticacion, InterfazGestionInventario):
    def login(self):
        print("✅ [ISP] Gerente de inventario ha iniciado sesión.")

    def registrar_entrada_producto(self):
        print("✅ [ISP] Gerente está registrando la entrada de nuevo inventario.")
