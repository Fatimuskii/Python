#SIntaxis de condicional IF (<,>,==, <=,>=, !=)

print("Programa de Evaluacion de notas de alumnos")
nota_alumno=int(input())

#cualquier dato que metamos con input python lo considera como un string


def evaluacion(nota): 
	valoracion="Aprobado"
	if nota<5:
		valoracion="suspenso"
	return valoracion

print(evaluacion(nota_alumno))

