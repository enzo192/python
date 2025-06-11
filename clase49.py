# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract the second number from the first
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide the first number by the second
# Raises an error if the divisor is zero
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    print('Operaciones')
    res_1 = add(3,4)
    print(f'Suma: {res_1}')  # Output: Suma: 7
    print(divide(10,7))  # Output: 1.4285714285714286
    
    
'''
Implemetar un archivo gestion_empleados.py que contenga
    1.Funciona para agregar y eliminar empleados de una lista

    2. Un bloque 'if __name__' == "main" que permita probar el
    funcionamiento del script ejecuatado directamente
'''

employeers = [
    {'name': 'Carlos', 'role': 'admin'},
    {'name': 'Juan', 'role': 'employee'},
    {'name': 'Jose', 'role': 'employee'},
    {'name': 'Ana', 'role': 'employee'}
]


def delete_employeer(employeers: list[dict], name_employeer: str):
    for employeer in employeers:
        if (employeer["name"] == name_employeer):
            employeers.remove(employeer)
            return True
    return False


def add_amployeer(employeers: list[dict], name: str, role: str):
    employeers.append({"name": name,"role": role})

if __name__ == "__main__":
    print(delete_employeer(employeers, "Juan"))
    print(employeers)
    add_amployeer(employeers, "Antonio", "admin")
    print(employeers)
    
    