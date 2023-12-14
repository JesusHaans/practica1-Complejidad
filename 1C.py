#imports
import random
import sys

# Variables globales
FILE_NAME = "ENTRADA1.txt"
#particiones de V
P1=[]
P2=[]

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

#verificamos que tengamos entre 10 y 20 vertices
if not (len(vertices) >= 10 and len(vertices) <= 20):
    print("La grafica no tiene el tamaño necesario en vertices")
    sys.exit(0)
    
#verificamos que tengamos entre 20 y 40 aristas
if not (len(aristas) > 2*len(vertices)):
    print("La grafica no tiene el tamaño necesario en aristas")
    sys.exit(0)

#Hagamos la fase adivinadora

def faseAdivinadora(vertices):
    for v in vertices:
        i = random.randint(0,100)
        if(i%2 == 0):
            P1.append(v)
        else:
            P2.append(v)
    print("Terminando la fase adivinadora las particiones quedan asi...")
    print("Particion P1 = " + ' '.join(P1))
    print("Particion P2 = " + ' '.join(P2))

def faseVerificadora(P1,P2,aristas):
    resultado = verificaAdyacencia(P1,aristas) and  verificaAdyacencia(P2,aristas)
    print("¿P1 y P2 son una biparticion de G?")
    print(resultado)

def verificaAdyacencia(P1,aristas):
    resultado = True
    for vi in P1:
        for vj in P1:
            if (vi,vj) in aristas:
                resultado = False
    return resultado



faseAdivinadora(vertices)
faseVerificadora(P1,P2,aristas)