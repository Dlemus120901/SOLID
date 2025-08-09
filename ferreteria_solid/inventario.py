# ferreteria_solid/inventario.py

class Producto:
    """Clase que representa un producto. Su única responsabilidad es modelar los datos del producto."""
    def __init__(self, sku: str, nombre: str, descripcion: str, precio: float, stock: int):
        self.sku = sku
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"Producto: {self.nombre} (SKU: {self.sku}) - Precio: ${self.precio:.2f}, Stock: {self.stock}"

class RepositorioProductos:
    """Clase responsable únicamente de la persistencia de los productos."""
    def guardar(self, producto: Producto):
        print(f"✅ [SRP] Guardando el producto '{producto.nombre}' en la base de datos.")

    def obtener_por_sku(self, sku: str) -> Producto:
        print(f"✅ [SRP] Obteniendo el producto con SKU {sku} de la base de datos.")
        # Simula la obtención de un producto
        return Producto(sku, "Taladro Inalámbrico", "Potente taladro de 18V", 99.99, 50)
