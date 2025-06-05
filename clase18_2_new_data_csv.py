import csv # importamos el módulo csv

# Definimos el nuevo producto como un diccionario
new_product = {
    'name': 'wireless charger',
    'price': 19,
    'quantity': 50,
    'brand': 'Samsung',
    'category': 'electronics',
    'entry_date': '2023-10-01',
}

# Abrimos el archivo CSV en modo 'a' (append) para agregar el nuevo producto
with open('products.csv', mode='a', newline='') as file:
    file.write('\n') # Añadimos una nueva línea para separar el nuevo producto
    csv_writer = csv.DictWriter(file, fieldnames = new_product.keys()) # Definimos los nombres de las columnas
    csv_writer.writerow(new_product) # Escribimos el nuevo producto en el archivo CSV