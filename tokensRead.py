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

def isInteger(j[i]):
isInteger(j[i])

def isFloat(j[i]):
isFloat(j[i])

def isOperatorEqual(j[i]):
isOperatorEqual(j[i])

def isOperatorAdd(j[i]):
isOperatorAdd(j[i])

def isOperatorSub(j[i]):
isOperatorSub(j[i])

def isOperatorMult(j[i]):
isOperatorMult(j[i])

def isOperatorDiv(j[i]):
isOperatorDiv(j[i])

def isOperatorPow(j[i]):
isOperatorPow(j[i])

def isParenthesisInitial(j[i]):
isParenthesisInitial(j[i])

def isParenthesisFinal(j[i]):
isParenthesisFinal(j[i])

def isComment(j[i]):
isComment(j[i])

def isVariable(j[i]):

isVariable(j[i])



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

                elif isOperatorEqual(j[i]):

                elif isOperatorAdd(j[i]):

                elif isOperatorSub(j[i]):

                elif isOperatorMult(j[i]):

                elif isOperatorDiv(j[i]):

                elif isOperatorPow(j[i]):

                elif isParenthesisInitial(j[i]):

                elif isParenthesisFinal(j[i]):

                elif isComment(j[i]):

                def isVariable(j[i]):


                
            
#apply exec() method
# exec("%s = %d" % (str,5000)) función para parametizar si es variable

# Generar un if para asignar // como un comentario
    print(caracteres)



lexerAritmetico(lineas)










































