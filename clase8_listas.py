#se crean con corchetes y se pueden modificar, son mutables. Tipo 'list'
to_do = ["Dirigirnos al hotel",
         "Ir a almorzar",
         "Visitar un museo",
         "Volver al hotel"]
print(to_do)

numbers = [1,2,3,4, "cinco"]
print(type(numbers))

mix = ["uno", 2, 3.14, True, [1,2,3]]
print(mix)

#cantidad de elementos en la lista
print(len(mix))

#indexacion, trallendo elemento especifico de la lista
print("Primer elemento", mix[0])
print("Segundo elemento", mix[1])
print("Ultimo elemento:", mix[-1])

#indexacion, trallendo elemento especifico del string
string = "Hola mundo"
print("Primer elemento", string[0])
print("Segundo elemento", string[1])
print("Ultimo elemento:", string[-1])
#imprime desde un elemento inicial hasta uno final
print(mix[2:-2])
print(mix)
#agregamos un elemento al final de la lista con el metodo .append
mix.append(False)
print(mix)
#agregamos una lista
mix.append(["a","b"])
print(mix)
#agregamos elementos con el metodo .insert en una posicion especifica que elegimos
mix.insert(1,["a","b"])
print(mix)
#con .index podemos obtener la ubicacion de la primera aparicion de un elemento
print(mix.index(["a","b"]))

numbers = [1,2,100.01,90.45,3,4, 5]
print(numbers)
print("Mayor:",max(numbers)) #numero mayor de la lista
print("Menor:",min(numbers)) #numero menor de la lista
#borramos elementos de la lista con del
del numbers[-1]
print(numbers)
del numbers[:2]
print(numbers)
del numbers #eliminamos la lista
#print(numbers)