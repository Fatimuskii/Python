#Diccionarios (Clave: Valor)
midiccionario={"Alemania":"Berlín", "Francia":"París", "Reino Unido": "Londres", "España": "Madrid"}
print(midiccionario["Francia"])


#Agregar elementos
midiccionario["Italia"]="Lisboa"

#modificar un valor de una claveç
	#sobreescribe el valor
midiccionario["Italia"]="Roma"

print(midiccionario)

#eliminar un elemento
del midiccionario ["Reino Unido"]
print(midiccionario)

#asignacion de tuplas/listas para asignar los valores de un diccionario

mitupla=("España", "Francia", "Reino Unido", "Alemania")
midiccionario={mitupla[0]:"Madrid", mitupla[1]:"Paris", mitupla[2]:"London", mitupla[3]:"Berlin"}

print(midiccionario) 

#Se pueden meter diccionarios dentro de diccionarios.

#claves de los diccionarios
print(midiccionario.keys())
print(midiccionario.values())
print(len(midiccionario))
