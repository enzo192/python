#cadenas o string = str

name = 'CARLA Marcela'
last_name = '   Florida     Roman  '
print(name[0]) #C
print(name[-1]) #a
print(5 * name) #CARLA MarcelaCARLA MarcelaCARLA MarcelaCARLA MarcelaCARLA Marcela
print(name + ' ' + last_name) #CARLA Marcela    Florida     Roman  
print(len(name)) #13
#contar caracteres con FUNCION len
print(len(last_name)) #22
#todo a minuscula con  METODO .lower
print(name.lower()) #carla marcela
#poner todo en mayus con METODO .upper
print(name.upper()) #CARLA MARCELA
#eliminar espacios con METODO .strip
print(last_name.strip()) #Florida     Roman