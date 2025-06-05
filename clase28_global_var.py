x = 5 #variable global

def modify_global():
    global x  # Declara que se usará la variable global x
    x += 3  # Modifica el valor de la variable global
    print(f'Valor modificado: {x}')
    
modify_global()  # Llama a la función que modifica la variable global
print(x)  # Imprime el valor de la variable global después de la modificación

