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

        for i in caracteres:
            
            #Asegurarse que lo primero que cheque si es comentario con una variable que revise si es verdadero o falso
            Comment = False

            for j in range(len(i)):

                if Comment == True: 
                
                elif isInteger(j[i]):

                elif isFloat(j[i]):

                elif isOperator(j[i]):

                elif isParenthesisInitial(j[i]):

                elif isParenthesisFinal(j[i]):

                elif isComment(j[i]):

                elif isVariable(j[i]):


                
            
#apply exec() method
# exec("%s = %d" % (str,5000)) función para parametizar si es variable

# Generar un if para asignar // como un comentario
    print(caracteres)



lexerAritmetico(lineas)










































