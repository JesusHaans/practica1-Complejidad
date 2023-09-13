# Variables globales
FILE_NAME = "ENTRADA1.txt"

#Abrimos el archivo
file = open(FILE_NAME)

#La primera linea la guardamos para trabajarla despues
strVertices = file.readline()
strVertices = strVertices[:-1]

#Llenamos las aristas con tuplas que representan las aristas
aristas = []
linea = file.readline()
while (linea != ''):
    aristas.append((linea[0],linea[2]))
    linea = file.readline()

#Trabajamos str Vertices
vertices = strVertices.split(',')


print(vertices)
print(aristas[0])
print(aristas[len(aristas)-1])