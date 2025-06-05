def outer_funtion():
    x = 'enclosing'
    
    def inner_function():
        nonlocal x  
        x = 'modified'  
        print(f'El valor en inner es: {x}')  
    
    inner_function()  # Llama a la función interna
    print(f'El valor outer es: {x}')  # Imprime la variable de la función externa
    
outer_funtion()  # Llama a la función externa