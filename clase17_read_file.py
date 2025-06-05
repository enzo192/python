#Leer un archivo linea por línea
"""
with open('cuento.txt', 'r') as file: # abre el archivo en modo lectura
    for line in file: # lee línea por línea del archivo
        print(line.strip()) # strip() elimina los espacios en blanco al principio y al final de la línea
"""
#leer todas las líneas en una lista
"""
with open('cuento.txt', 'r') as file: # abre el archivo en modo lectura
    lines = file.readlines() # lee todas las líneas del archivo
    print(lines) # imprime la lista de líneas"""
    
#agregando informacion al texto
""" 
with open('cuento.txt', 'a') as file: # abre el archivo en modo escritura y la 'a' significa append
    file.write('\n\nBy: ChatGPT') # escribe una línea en el archivo .txt 
    """
    
    
#sobreescribiendo el archivo
""" 
with open('cuento.txt', 'w') as file: # abre el archivo en modo escritura y la 'w' significa write
    file.write('\n\nBy: ChatGPT') # escribe una línea en el archivo .txt
 """

#conteo de lineas del archivo
with open('cuento.txt', 'r') as file: # abre el archivo en modo lectura
    lines = file.readlines() # lee todas las líneas del archivo
    print(len(lines)) # imprime la cantidad de líneas
