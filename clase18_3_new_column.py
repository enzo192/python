import csv # importamos el módulo csv

file_path = 'products.csv' # Definimos la ruta del archivo CSV original
updated_file_path = 'products_updated.csv' # Definimos la ruta del nuevo archivo CSV

with open(file_path, mode='r') as file: # Abrimos el archivo CSV original en modo lectura
    csv_reader = csv.DictReader(file)
    # obtener los nombres de las columnas
    fieldnames = csv_reader.fieldnames + ['total_value'] # Añadimos una nueva columna 'total_value'
    
    # Abrimos el nuevo archivo CSV en modo escritura
    with open(updated_file_path, mode='w', newline='') as updated_file: 
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames) # Definimos los nombres de las columnas
        csv_writer.writeheader() # escribir los encabezados
        
        for row in csv_reader: # Iteramos sobre cada fila del archivo original
            # calcular valor total
            row['total_value'] = float(row['price']) * int(row['quantity'])
            csv_writer.writerow(row) # escribir la fila actualizada
# El archivo 'products_updated.csv' ahora contiene una nueva columna 'total_value'

