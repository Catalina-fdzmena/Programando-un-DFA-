"""
Programando un DFA

Integrantes:
Santiago Andrés Serrano Vacca       A01734988
Ana Paula Pedroza Ramírez           A00830553
Andrea Catalina Fernández Mena      A01197705
Thomas Freund Paternostro           A00831997

"""

# Abrir el archivo
file = open("ejemplo.txt", 'r')

# En esta función, se valida si el token es un entero, en caso de que
# sea cierto, se retorna un true y en caso de que no lo sea se retorna false
def isInt(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

# Esta funcion valida que el token sea un operador aritmético y en caso de que 
# lo sea, se retorna el operador.
def isOperator(char):
    operadores = ['+', '-', '*', '/', '%', '^', '=']
    return (char in operadores)

# La función valida que el numero sea float, si no lo es se retorna false y si si lo es
# se retorna el . en num
def isFloat(num):
    try:
        float(num)
    except ValueError:
        return False
    return('.' in num)

# Esta función valida que el token sea una variable (que empiece con letras y solo esté formada por letras y underscores)
# En caso de que sea una variable se retorna verdadero.
def isVar(char):
    try:
        float(char)
        return False
    except ValueError:
        return True

# Las siguientes dos funciones se aseguran que el token sea un paréntesis y en caso de que lo sea
# se retorna el paréntesis
def isRightParentesis(char):
    parentesis = ['(']
    return(char in parentesis)

def isLeftParentesis(char):
    parentesis2 = [')']
    return(char in parentesis2)

# La función valida que el token sea un comentario, en caso de que lo sea se devuelve un true.
def isComentario(char):
    return (char == '//')

# Esta función se dedica a pasar por cada uno de los carácteres de la lista para despues pasarlos por
# casa una de las funciones anteriores hasta que estas sean verdaderas.
def checarCaracteres(lista):
    for char in lista:
        # En esta función se hace un break porque el comentario ocupa el resto del renglón.
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
        elif isOperator(char):
            print('Operator : ' + char)
        elif isVar(char):
            print('Variable : ' + char)
        elif isFloat(char):
            print('Float : ' + char)
        elif isInt(char):
            print('Integer : ' + char)

# se leen todas las lineas del documento y se devuelven como si cada linea fuera un item de la lista
lineas = file.readlines()

caracteres = []

# Se agrega carácteres a cada split de las lineas de la lista
for i in range(len(lineas)):
   caracteres.append(lineas[i].split())
   
print(caracteres)

# Se manda a llamar la función principal
for i in caracteres:
    checarCaracteres(i)
