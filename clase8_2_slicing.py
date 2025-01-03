#cuando copias una lista se copia
# la informacion pero tambien el espacio 
# en memoria en el que se guarda la variable
# El Slicing es para solo copiar la info pero
# sin apuntar al mismo espacio de memoria
# Lista de ejemplo
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Ejemplos de slicing
sublista1 = lista[2:5]
sublista2 = lista[:4]
sublista3 = lista[5:]
sublista4 = lista[::2]
sublista5 = lista[1:7:2]

# Slicing con índices negativos
sublista6 = lista[-5:]
sublista7 = lista[:-5]
sublista8 = lista[-8:-2:2]

# Salida de resultados
print("Lista original:", lista)
print("Sublista del índice 2 al 4:", sublista1)
print("Sublista desde el inicio al índice 3:", sublista2)
print("Sublista desde el índice 5 al final:", sublista3)
print("Sublista con paso de 2:", sublista4)
print("Sublista del índice 1 al 6 con paso de 2:", sublista5)
print("Últimos 5 elementos:", sublista6)
print("Todos menos los últimos 5:", sublista7)
print("Sublista del índice -8 al -3 con paso de 2:", sublista8)


'''explicación del Código

1. **Lista de Ejemplo**: Se define una lista de ejemplo con 10 elementos.
2. **Slicing Básico**: Se crean sublistas utilizando diferentes 
combinaciones de índices de inicio, fin y paso.
3. **Slicing con Índices Negativos**: Se muestran ejemplos de cómo utilizar índices 
negativos para acceder a elementos desde el final de la lista.
4. **Salida de Resultados**: Se imprimen las sublistas resultantes para visualizar 
los efectos de cada operación de slicing.

Este script te proporciona una comprensión completa de cómo utilizar el método `slice` para manipular listas en Python.
'''