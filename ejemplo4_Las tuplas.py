#Son listas inmutables, es decir, no se pueden modificar despues de su creacion
# no perminten añadir, eliminar, mover elementos (no append, exten, remove)
# si permiten extraer porciones, pero el resultado de la extraccion es una tupla nueva
# si permiten comprobar si un elemento esta en la tupla

# nombreLiSTA=(elem1, elem2, elem3)

mitupla=("Juan", 13, 1, 1995)
print(mitupla[2])

#convertir una lista a tupla o tupla a lista
	#nota: sabemos que es una lista por los corchetes []
milista=list(mitupla)
print(milista) 

milista1=["Milista", 13,2]
mitupla2=tuple(milista1)
print(mitupla2)

#encontrar un elemento en una tupla
	#devolvera True/False
print ("Juan" in mitupla)

#metodo count, cuantos elementos hay un elemento. 	
print (mitupla.count(13))

#metodo len. para la longitud de la tupla (num elementos)
print (len(mitupla))

#tupla UNITARIA 
tuplaUnitaria=("Juan",)

#empaquetado/desempaquetado de una tupla
nombre, dia, mes, agno=mitupla

	#esto asigna directamente por orden a estas variables en estas variables
	#desempaquetado de tupla

mitupla3="Juana", 2, 3, 1996 
print(mitupla3)
nombre1,dia1,mes1,agno1=mitupla3


