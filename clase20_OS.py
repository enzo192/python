import os
# CDW = current working directory
# obtener el directorio de trabajo actual
cwd = os.getcwd()
""" print("Directorio de trabajo actual:", cwd)
 """

#listar los archivos .txt en el directorio actual
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
""" print("Archivos txt:", txt_files)
 """

#cambiar nombre de un archivo
os.rename('cuento.txt', 'cuento2.txt') # Renombrar el archivo cuento.txt a cuento2.txt
print("Archivo renombrado de cuento.txt a cuento2.txt")