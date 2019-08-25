#PYTHON PASA LOS PARAMETROS POR REFERENCIA

#Funcion con mas de 1 param sin retorno
def suma(num1,num2):
	print(num1+num2)

#Funcion con mas de 1 param CON retorno
def suma1(num1,num2):
	resultado =num1+num2
	return resultado


suma(2,5)
suma("Pepe", " es tonto")
print (suma1(2,5))
print (suma1("Pepe", " ES TONTO"))