file = open("ejemplo.txt", 'r')


import operator

ops = {
    '+' : operator.add ,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}

lineas = file.readlines()
caracteres = []

def lexerAritmetico(lineas):
    for i in range(len(lineas)):
        caracteres.append(lineas[i].split())
        print(caracteres)

    #for i in caracteres:
        #for j in range(len(i)):
            
#apply exec() method
# exec("%s = %d" % (str,5000)) función para parametizar si es variable

# Generar un if para asignar // como un comentario









































