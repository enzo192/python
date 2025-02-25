#Leer un archivo linea por línea
"""
with open('cuento.txt', 'r') as file: # abre el archivo en modo lectura
    for line in file: # lee línea por línea del archivo
        print(line.strip()) # strip() elimina los espacios en blanco al principio y al final de la línea
"""
#leer todas las líneas en una lista
"""with open('cuento.txt', 'r') as file: # abre el archivo en modo lectura
    lines = file.readlines() # lee todas las líneas del archivo
    print(lines) # imprime la lista de líneas"""
    
#escribir en un archivo
with open('cuento.txt', 'a') as file: # abre el archivo en modo escritura
    file.write('\n\nBy: ChatGPT') # escribe una línea