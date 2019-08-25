#LAS LISTAS
#En python pueden guardar diferente tipo de valores
# Se pueden expandir dinamicamente.

milista=["Juan","Maria","Pepe","Marta"]

#imprimir toda la lista
print( milista[:])

#acceder a un elemento
print(milista[2])

#INDICE NEGATIVO, empieza por atras empiezando pos 1...
print (milista[-2])

#porcion de lista, para acceder a una parte de una lista
#incluye el primero, excluye el segundo
print (milista[0:1]) # li mismo que poner[:1]

#AÑADIR ELEMENTO al final de la lista
milista.append("Fatima")

#añadir un elemento en otro lugar: (indice,valor)
milista.insert(2,"Fatima2")

#añadir varios elementos al final de la lista== es concatenar otra lista
#tambien se puede concatenar dos listas con +. milista3= milista1+milista2,  guarda en milista3 todos los valores de milista1 y milista2

milista.extend(["ana","juana","irene"])

milista3=["ejem1","ejem2",4]* 3 #crea milista3 con esos 3 valores, tres veces

#identificar el Indice de un valor
milista.index("ana")

#identificar si un valor esta en la lista o no
print("Fatima" in milista) #mira si el valor Fatima esta en la lista, devolvera True/False


#Eliminar elementos por valor
milista.remove("Fatima")
#Eliminar el ultimo elemento de la lista
milista.pop()

