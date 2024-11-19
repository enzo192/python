#   Uso del print
#       El uso mas basico del print es el de imprimir el texto que quieres imprimir
print("Hola mundo\n")


#    Uso de las comillas
#       Utilizado para separar varios argumentos añadiendo autimaticamente los espacios entre los argumentos
#       ¡¡¡CUIDADO!!! esto es totalmente diferente a CONCATENAR, en este NO se añaden los espacios 
print("Hola", "mundo", "como","estan?\n") 

#    Uso del SEP
#       Lo utilizamos para poder especificar  el tipo de separador que se va a usar entre los elementos
#       por se utiliza un espacio simple (' ')
print ("Hola", "mundo", "como", "estan?\n", sep="_" )
 
#     Uso del END  
#       Espefica lo que se imprimira al final de la cadena. Puedes cambiar como deseas acabar la cadena
#       puedes  evitar saltos de linea, agregar espacios, tabulaciones.
print("Hola", end="@")
print("mundo\n")

#     f-string
#       Podemos incluir expresiones dentro de las cadenas, insertando valores o expresiones directamente en 
#       la cadena
#           SINTAXIS   
#               se coloca una f o F al antes de las comillas para luego encerrar las expreciones dentro de
#               unas llaves {}
nombre = "Juan" 
edad = 30

print(f"Me llamo {nombre} y tengo {edad} años\n")

#     Formato
#       Es otra forma de insertar valores similares a f-string
frase = "nunca pares de aprender"
autor = "platzi"
print("frase: {}, autor: {}\n".format(frase,autor))

#     Formatos especificos 
#       Controlasmos el formato en que se va a imprimir los numeros 

#valor : 3.14159
#print("Valor: {:.2f}".format(valor))

#     Salto de linea y caracteres especiales 
#           los saltos de linea se indican con un \n al final de la cadena 
print("Hola\nmundo")

#           Para imprimir unas commilas dobles o simples ocupamos diagonales (\) antes de las comillas
print('Hola soy \'carli\'\n')

#           Para imprimir una diagonal ocupamos dobles diagonales (\\)