# main.py
from ferreteria_solid.inventario import Producto, RepositorioProductos
from ferreteria_solid.pos import Venta, DescuentoPorcentaje, DescuentoMontoFijo
from ferreteria_solid.proveedores import ProveedorLocal, ProveedorInternacional
from ferreteria_solid.personal import Cajero, GerenteInventario
from ferreteria_solid.reportes import GeneradorReportes, BaseDatosVentas, ArchivoCsvVentas

def run_demo():
    """
    Función principal para ejecutar la demostración de los principios SOLID.
    """
    print("--- 🚀 INICIO DE LA DEMOSTRACIÓN DEL DISEÑO SOLID 🚀 ---\n")

    # 1. Principio de Responsabilidad Única (SRP)
    print("="*50)
    print("1. PRINCIPIO DE RESPONSABILIDAD ÚNICA (SRP)")
    print("   Una clase para datos (Producto) y otra para persistencia (RepositorioProductos).\n")
    producto = Producto("HM-001", "Martillo de bola", "Acero forjado", 25.00, 120)
    repositorio = RepositorioProductos()
    print(producto)
    repositorio.guardar(producto)
    print("\n")

    # 2. Principio de Abierto/Cerrado (OCP)
    print("="*50)
    print("2. PRINCIPIO DE ABIERTO/CERRADO (OCP)")
    print("   La clase Venta está cerrada a cambios, pero abierta a extenderse con nuevos descuentos.\n")
    venta = Venta(200.00)
    venta.agregar_descuento(DescuentoPorcentaje(10)) # 10% de 200 = 20
    venta.agregar_descuento(DescuentoMontoFijo(15)) # 15 fijos
    total_final = venta.calcular_total_final()
    print(f"✅ [OCP] Total inicial: $200.00")
    print(f"✅ [OCP] Aplicando un descuento del 10% y uno de $15.00.")
    print(f"✅ [OCP] Total final: ${total_final:.2f} (200 - 20 - 15 = 165)")
    print("\n")

    # 3. Principio de Sustitución de Liskov (LSP)
    print("="*50)
    print("3. PRINCIPIO DE SUSTITUCIÓN DE LISKOV (LSP)")
    print("   Podemos usar subclases de Proveedor (Local, Internacional) donde se espera la clase base.\n")
    proveedores = [
        ProveedorLocal("Tornillos de Guatemala S.A."),
        ProveedorInternacional("Global Tools Inc.")
    ]
    for p in proveedores:
        p.procesar_orden_compra() # Se llama al mismo método en objetos de diferentes tipos
    print("\n")
    
    # 4. Principio de Segregación de Interfaces (ISP)
    print("="*50)
    print("4. PRINCIPIO DE SEGREGACIÓN DE INTERFACES (ISP)")
    print("   Cada rol (Cajero, Gerente) implementa solo las interfaces que necesita.\n")
    cajero = Cajero()
    gerente = GerenteInventario()
    cajero.login()
    cajero.realizar_cobro()
    print("-" * 20)
    gerente.login()
    gerente.registrar_entrada_producto()
    print("\n")

    # 5. Principio de Inversión de Dependencia (DIP)
    print("="*50)
    print("5. PRINCIPIO DE INVERSIÓN DE DEPENDENCIA (DIP)")
    print("   El GeneradorReportes depende de una abstracción (FuenteDatos), no de una BD o un CSV concretos.\n")
    
    # Demostración con base de datos
    fuente_bd = BaseDatosVentas()
    reportador_bd = GeneradorReportes(fuente_bd)
    reportador_bd.generar_reporte_ventas()
    print("-" * 20)

    # Demostración con archivo CSV
    fuente_csv = ArchivoCsvVentas()
    reportador_csv = GeneradorReportes(fuente_csv)
    reportador_csv.generar_reporte_ventas()
    print("\n")

    print("--- ✨ FIN DE LA DEMOSTRACIÓN ✨ ---")


if __name__ == "__main__":
    run_demo()
