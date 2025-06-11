# Definimos un decorador llamado log_transaction que recibe una función como argumento
def log_transaction(func):
    # Definimos una función interna (wrapper) que envuelve la función original
    def wrapper():
        print('1 Log de la transacción...')  # Imprime un mensaje antes de ejecutar la función original
        func()                              # Llama a la función original
        print('3 Log terminado...')          # Imprime un mensaje después de ejecutar la función original
    return wrapper                           # Retorna la función interna (decorada)
        

# Aplicamos el decorador log_transaction a la función process_payment
@log_transaction
def process_payment():
    print('2 Procesando pago....')           # Imprime un mensaje indicando que se está procesando el pago

# Llamamos a la función decorada process_payment
process_payment()