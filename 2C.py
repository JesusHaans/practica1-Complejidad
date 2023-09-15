#imports
import random
import re

# Variables globales
FILE_NAME = "ENTRADA2.txt"
variables = []
varDic = {}


#Abrimos el archivo
file = open(FILE_NAME)

#La primera linea la guardamos para trabajarla despues
linea = file.readline()
variablesRepetidas = re.findall('\w+',linea)
#Limpiar Repeticiones
for var in variablesRepetidas:
    if var not in variables:
        variables.append(var)
conjunciones = linea.split('*')

#
def itsFalse(variables,varDic):
    result  = False
    for var in variables:
        if var[0] == '-':
            result = result or  (not varDic[var[1:]])
        else:
            result = result or (varDic[var])
    if result == True: 
        return False 
    else:
        return True 

def procesarClausula(cadena):
    preCadena = cadena.replace('(','')
    finalCadena = preCadena.replace(')','')
    variables = finalCadena.split('+')
    return variables

def ND_Choice():
    i = random.randint(0,100)
    if i%2 == 0:
        return True
    else:
        return False

def faceAdivinadora(variables, varDic):
    for var in variables:
        varDic[var] = ND_Choice()
    print("Terminando la fase adivinadora los valores quedan asi...")
    print("Variables: " + str(varDic))

def faceVerificadora(varDic, conjunciones, linea):
    print("¿" + str(varDic) +" satisface la formula: " + linea + "?")
    for c in conjunciones:
        variables = procesarClausula(c)
        if itsFalse(variables,varDic):
            print("False")
            return
    print("True")

faceAdivinadora(variables, varDic)
faceVerificadora(varDic,conjunciones,linea)
#itsFalse(['x', '-y', 'z'],varDic)
