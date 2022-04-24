"""
Programando un DFA

Integrantes:
Santiago Andrés Serrano Vacca       A01734988
Ana Paula Pedroza Ramírez           A00830553
Andrea Catalina Fernández Mena      A01197705
Thomas Freund Paternostro           A00831997

"""


file = open("ejemplo.txt", 'r')

def isInt(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

"""def isOperator(char):
    operadores = ['+', '-', '*', '/', '%', '^']
    return (char in operadores)"""

def isSuma(char):
    suma = ['+']
    return(char in suma)

def isResta(char):
    resta = ['-']
    return(char in resta)

def isMultiplicacion(char):
    multi = ['*']
    return(char in multi)

def isDivision(char):
    div = ['/']
    return(char in div)

def isPow(char):
    pow = ['^']
    return(char in pow)

def isPorcentaje(char):
    porcentaje = ['%']
    return(char in porcentaje)

def isAsignacion(char):
    asignacion = ['=']
    return(char in asignacion)

def isFloat(num):
    try:
        float(num)
    except ValueError:
        return False
    return('.' in num)

def isVar(char):
    try:
        float(char)
        return False
    except ValueError:
        return True

def isRightParentesis(char):
    parentesis = ['(']
    return(char in parentesis)

def isLeftParentesis(char):
    parentesis2 = [')']
    return(char in parentesis2)

def isComentario(char):
    return (char == '//')

def lexerAritmetico(tokenList):
    for char in tokenList:
        if isComentario(char):
            index = tokenList.index(char)
            print('Comentario : //')
            for i in range(index+1, len(tokenList)):
                print(tokenList[i])
            break
        elif isRightParentesis(char):
            print(('Parentesis de abre: ('))
        elif isLeftParentesis(char):
            print(('Parentesis de cierra: )'))
        elif isSuma(char):
            print(('Suma: +'))
        elif isResta(char):
            print(('Operador Resta: -'))
        elif isMultiplicacion(char):
            print(('Operador Multiplicacion: *'))            
        elif isDivision(char):
            print(('Operador Division: /'))
        elif isPow(char):
            print(('Operador Potencia: /'))
        elif isAsignacion(char):
            print(('Asignacion: ='))
        elif isPorcentaje(char):
            print(('Operador Porcentaje: %'))
        #elif isOperator(char):
            #print('Operator : ' + char)
        elif isVar(char):
            print('Variable : ' + char)
        elif isFloat(char):
            print('Float : ' + char)
        elif isInt(char):
            print('Entero : ' + char)

lineas = file.readlines()

caracteres = []

for i in range(len(lineas)):
   caracteres.append(lineas[i].split())
   
print(caracteres)

for i in caracteres:
    lexerAritmetico(i)