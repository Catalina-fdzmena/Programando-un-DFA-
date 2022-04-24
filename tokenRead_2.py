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

def isOperator(char):
    operadores = ['+', '-', '*', '/', '%', '^']
    return (char in operadores)

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

def isAsignacion(char):
    asignacion = ['=']
    return(char in asignacion)

def isRightParentesis(char):
    parentesis = ['(']
    return(char in parentesis)

def isLeftParentesis(char):
    parentesis2 = [')']
    return(char in parentesis2)

def isComentario(char):
    return (char == '//')

def lexerAritmetico(lista):
    for char in lista:
        if isComentario(char):
            index = lista.index(char)
            print('Comentario : //')
            for i in range(index+1, len(lista)):
                print(lista[i])
            break
        elif isRightParentesis(char):
            print(('Right Parenthesis: ('))
        elif isLeftParentesis(char):
            print(('Left Parenthesis: )'))
        elif isAsignacion(char):
            print(('Asignation: ='))
        elif isOperator(char):
            print('Operator : ' + char)
        elif isVar(char):
            print('Variable : ' + char)
        elif isFloat(char):
            print('Float : ' + char)
        elif isInt(char):
            print('Integer : ' + char)

lineas = file.readlines()

caracteres = []

for i in range(len(lineas)):
   caracteres.append(lineas[i].split())
   
print(caracteres)

for i in caracteres:
    lexerAritmetico(i)