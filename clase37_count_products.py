# estructuras de datos avanzados:  collections y enumeraciones
from collections import defaultdict

def count_products(orders: list[str]) -> defaultdict: # definimos el tipo de dato de la lista como str
    #Crea un diccionario con valor por defecto 0 
    product_count = defaultdict(int) # defaultdict crea un diccionario que devuelve 0 si la clave no existe
    for product in orders: # Iteramos sobre cada producto en la lista de pedidos
        product_count[product] +=1 # Incrementamos el contador del producto en el diccionario
    return product_count # Devolvemos el diccionario con los conteos de productos

# Ejemplo de uso

orders = ['laptop', 'smartphone', 'laptop', 'tablet'] # Lista de pedidos de productos
count = count_products(orders) # Llamamos a la función para contar los productos
print(count) # Imprimimos el resultado del conteo de productos
# Resultado esperado: defaultdict(<class 'int'>, {'laptop': 2, 'smartphone': 1, 'tablet': 1})