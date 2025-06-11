#Sistema de gestión de pedidos utilizando colecciones y enumeraciones

from collections import deque # Importa la clase deque para manejar colas de pedidos
from enum import Enum # Importa Enum para definir enumeraciones de estados de pedidos
from collections import defaultdict, Counter # Importa defaultdict y Counter para manejar inventario y contar productos
from typing import List, Dict, Any # Importa List, Dict y Any para anotaciones de tipos



# Define una enumeración para los estados de los pedidos
class OrderStatus(Enum):
    PENDING = "Pending"  # Estado pendiente
    SHIPPED = "Shipped"  # Estado enviado
    DELIVERED = "Delivered"  # Estado entregado

# Clase para manejar el inventario de productos
class ProductInventory:
    def __init__(self) -> None:
        # Diccionario para almacenar productos y sus cantidades
        self.products: Dict[str, int] = defaultdict(int)

    def add_products(self, products: List[str]) -> None:
        """
        Agrega productos al inventario.
        :param products: Lista de nombres de productos a agregar.
        """
        try:
            # Cuenta la cantidad de cada producto en la lista
            counter: Counter = Counter(products)
            # Suma la cantidad de cada producto al inventario
            for product, quantity in counter.items():
                self.products[product] += quantity
        except Exception as e:
            # Muestra un error si ocurre una excepción
            print(f"Error adding products: {e}")

    def show_inventory(self) -> None:
        """Muestra el inventario actual de productos."""
        print("Product Inventory:")  # Imprime el encabezado
        # Recorre e imprime cada producto y su cantidad
        for product, quantity in self.products.items():
            print(f"{product}: {quantity}")

# Clase que representa un pedido
class Order:
    def __init__(self, order_id: int, customer: str, products: List[str]) -> None:
        """
        Inicializa un pedido.
        :param order_id: Identificador único del pedido.
        :param customer: Nombre del cliente.
        :param products: Lista de productos en el pedido.
        """
        self.order_id: int = order_id  # Asigna el ID del pedido
        self.customer: str = customer  # Asigna el nombre del cliente
        self.products: List[str] = products  # Asigna la lista de productos
        self.status: OrderStatus = OrderStatus.PENDING  # Estado inicial pendiente

    def update_status(self, new_status: OrderStatus) -> None:
        """
        Actualiza el estado del pedido.
        :param new_status: Nuevo estado a asignar (debe ser OrderStatus).
        """
        try:
            # Verifica que el nuevo estado sea válido
            if isinstance(new_status, OrderStatus):
                self.status = new_status  # Actualiza el estado
            else:
                # Lanza un error si el tipo es incorrecto
                raise ValueError("Invalid status type")
        except Exception as e:
            # Muestra un error si ocurre una excepción
            print(f"Error updating order status: {e}")

    def __str__(self) -> str:
        # Devuelve una representación en texto del pedido
        return f"Order {self.order_id} - Customer: {self.customer} - Status: {self.status.value}"

# Clase para gestionar los pedidos y el inventario
class OrderManager:
    def __init__(self) -> None:
        # Cola para almacenar los pedidos
        self.orders: deque[Order] = deque()
        # Instancia del inventario de productos
        self.inventory: ProductInventory = ProductInventory()

    def add_order(self, order: Order) -> None:
        """
        Agrega un pedido a la cola y actualiza el inventario.
        :param order: Objeto Order a agregar.
        """
        try:
            self.orders.append(order)  # Agrega el pedido a la cola
            self.inventory.add_products(order.products)  # Actualiza el inventario
        except Exception as e:
            # Muestra un error si ocurre una excepción
            print(f"Error adding order: {e}")

    def process_order(self) -> Any:
        """
        Procesa el siguiente pedido en la cola cambiando su estado a SHIPPED.
        :return: El objeto Order procesado o None si no hay pedidos.
        """
        try:
            # Verifica si hay pedidos en la cola
            if self.orders:
                order: Order = self.orders.popleft()  # Saca el primer pedido de la cola
                order.update_status(OrderStatus.SHIPPED)  # Cambia el estado a enviado
                return order  # Devuelve el pedido procesado
            return None  # Devuelve None si no hay pedidos
        except Exception as e:
            # Muestra un error si ocurre una excepción
            print(f"Error processing order: {e}")
            return None

    def list_orders(self) -> None:
        """Imprime todos los pedidos actualmente en la cola."""
        # Recorre e imprime cada pedido en la cola
        for order in self.orders:
            print(order)

    def show_inventory(self) -> None:
        """Muestra el inventario actual."""
        self.inventory.show_inventory()  # Llama al método para mostrar inventario

# Ejemplo de uso
if __name__ == "__main__":
    manager: OrderManager = OrderManager()  # Crea un gestor de pedidos
    order1: Order = Order(1, "John", ["Pizza", "Soda"])  # Crea el primer pedido
    order2: Order = Order(2, "Anna", ["Burger", "Pizza"])  # Crea el segundo pedido
    manager.add_order(order1)  # Agrega el primer pedido
    manager.add_order(order2)  # Agrega el segundo pedido
    manager.list_orders()  # Lista los pedidos en la cola
    manager.show_inventory()  # Muestra el inventario actual
    processed = manager.process_order()  # Procesa el siguiente pedido
    if processed:
        print(f"Processing: {processed}")  # Imprime el pedido procesado
    manager.list_orders()  # Lista los pedidos restantes
    manager.show_inventory()  # Muestra el inventario actualizado

