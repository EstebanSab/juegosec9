Algoritmo Estudio_Deen
	Escribir 'Estamos contratando personal, solo tiene que responder unas preguntas'
	Escribir "¿Estas de acuerdo?"
	Leer Respuesta
	Si Respuesta='si' o Respuesta="Si" Entonces
		Escribir 'Que edad tienes? ' Nombre
		Leer Edad
		Si Edad>=18 Entonces
			Escribir 'Cual es tu nombre?'
			Leer Nombre
			Escribir 'Donde vives?'
			Leer Direccion
			Escribir 'Cual es su numero de celular?'
			Leer Numero
			Escribir 'Usted fue estafado'
			Escribir 'No debe brindar datos personales'
			Escribir "Ahora poseemos sus datos"
			Escribir Nombre " de " Edad " años"
			Escribir "Direccion " Direccion
			Escribir "Telefono " Numero
		SiNo
			Escribir "Solo aceptamos a personas mayores a 18" FinAlgoritmo
		Fin Si
	SiNo
		Escribir 'Gracias por su tiempo',FinAlgoritmo
	FinSi
FinAlgoritmo