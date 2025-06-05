import random

#generar numero entero aleatorio

random_number = random.randint(1, 10)
print(random_number)


#elegir colores aleatorios
colores = ['rojo', 'verde', 'azul', 'amarillo', 'naranja']
color_aleatorio = random.choice(colores)
print(color_aleatorio)

#barajar una lista de cartas
cards = ['corazones', 'diamantes', 'tréboles', 'picas','As','Rey','Reina','Joker']
random.shuffle(cards)
print(cards)

