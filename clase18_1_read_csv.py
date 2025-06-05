import csv

# leer un archivo CSV
""" with open('products.csv', mode='r') as file: # abrir el archivo en modo lectura
    csv_reader = csv.DictReader(file) # leer el archivo como un diccionario
    for row in csv_reader: # iterar sobre cada fila
        print(row) # imprimir cada fila""" 
        
# mostrar la informacion por columnas
with open('products.csv', mode='r') as file: # abrir el archivo en modo lectura
    csv_reader = csv.DictReader(file) # leer el archivo como un diccionario
    for row in csv_reader: # iterar sobre cada fila
        print(f"Producto: {row['name']}, Precio: {row['price']}") # clasificamos por columnas la informacion
        
