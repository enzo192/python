def sum_numbers(n):
    # Caso base: si n es 0, la suma es 0
    if n == 0:
        return 0
    # Caso recursivo: n + suma de (n-1)
    else:
        return n + sum_numbers(n - 1)

# Llamada a la función
result = sum_numbers(5)
print(f"Suma de los primeros 5 números es: {result}")

def fibonacci(n):
    # Caso base: si n es 0 o 1, la serie es 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: fibonacci(n-1) + fibonacci(n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)