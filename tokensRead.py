file = open("ejemplo.txt", 'r')

import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}

lineas = file.readlines()

caracteres = []

for i in range(len(lineas)):
    caracteres.append(lineas[i].split())

print(caracteres)


#apply exec() method
# exec("%s = %d" % (str,5000)) función para parametizar si es variable

# Generar un if para asignar // como un comentario






























































"""
#assign the operators

#use a dictionary


#leer archivo
file = open("tryOuts.py")

operators =  {"=" : "Asignación", '+': 'Suma', '/' : 'División', "^" : 'Potencia', '//' : 'Comentario', '*' : 'Multiplicación', '-' : 'Resta'}
operators_key = operators.keys()

specialSymbol = {"(" : 'Paréntesis que abre', ")" : 'Paréntesis que cierra' }
specialSymbol_key = specialSymbol.keys()

data_type = {'int' : 'integer type', 'float': 'Floating point' , 'char' : 'Character type', 'long' : 'long int' }
data_type_key = data_type.keys()

identifier = { 'a' : 'Variable', 'b' : 'Variable', 'c' : 'Variable' , 'd' : 'Variable' }

identifier_key = identifier.keys()

dataFlag = False

a=file.read()

count = 0 
program = a.split("\n")
for line in program:
    count = count + 1
    print("line#" , count, "\n" , line)

    #tokens=line.split('')
    print("Tokens are " , tokens)
    print("Line#", count, "properties \n")
    for token in tokens:
        isInt = True
        if token in operators_key:
            print(token, operators[token])
        if token in data_type_key:
            print(token, data_type[token])
        if token in identifier_key:
            print (token, identifier[token])
        if token in specialSymbol_key:
            print (token, specialSymbol[token])
        
        if token.isnumeric():
          try:
            int(token)
          except ValueError:
            float(token)
            float = {token : "Real"}
            print (token, float[token])
            isInt = False
          if  isInt:
              integer = {token : "Entero"}
              print (token, integer[token])

          

    dataFlag=False

"""
