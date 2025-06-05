import json

with open('products.json', mode='r') as file: # Abrimos el archivo JSON original en modo lectura
    products = json.load(file)  # Cargar el contenido del archivo JSON
    
#mostrar el contenido del archivo JSON
for product in products:
    #print(product)
    print(f"Product: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")