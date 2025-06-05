x = 'global' # Variable global

#funcion externa
def outer_function():
    x = 'enclosing'
    
    #funcion interna
    def inner_function():
        x = 'local' # Variable local
        print(x)
        
    inner_function()  # Llama a la función interna
    print(x)  # Imprime la variable de la función externa

outer_function()  # Llama a la función externa
print(x)  # Imprime la variable global

