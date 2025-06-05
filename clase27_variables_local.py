x = 100 # Variables globales

def local_funcion():
    # Variables locales
    x = 10
    print(f'el valor de la variable es {x}')

def show_global():
    # Variables globales
    print(f'el valor de la variable global es {x}')
    
local_funcion()
show_global()
print(x)  # Imprime la variable global