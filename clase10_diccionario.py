numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers[2])
information = {"nombre": "Carla",
               "Apellido": "Florida",
               "Altura": 1.60,
               "Edad": 29}
print(information)
del information["Edad"]
print(information)
claves = information.keys()
print(claves)
#print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)
contacts = {"Carla": {"Apellido": "Florida",
               "Altura": 1.60,
               "Edad": 29},
                "Diego": {"Apellido": "Antezana",
               "Altura": 1.80,
               "Edad": 32}}
print(contacts["Carla"])

#comprehension list
#una forma mas facil de hacer diccionarios

squares = [x**2 for x in range(1,11)]
#print("Cuadrados:", squares)

celsius = [0, 10, 20, 30, 40]
fahrenheit = [((9/5)*temp + 32) for temp in celsius]
#print("Temperatura en F: ", fahrenheit)

#Numeros pares
evens = [x for x in range(1,21) if x%2 == 0]
#print("Pares: ", evens)

matrix = [[1,2,3], 
          [4,5,6], 
          [7,8,9]]

transposed = [[row[i] for row in matrix] for i in range(3)]
print(matrix)
print(transposed)

