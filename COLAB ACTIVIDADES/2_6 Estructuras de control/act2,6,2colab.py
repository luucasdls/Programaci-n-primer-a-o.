calificaciones = input("Ingrese las calificaciones separadas por comas: ")

calificaciones = calificaciones.split(",")

aprobados = 0
desaprobados = 0
suma = 0

for nota in calificaciones:
    nota = float(nota)
    suma += nota

    if nota >= 7:
        aprobados += 1
    else:
        desaprobados += 1

promedio = suma / len(calificaciones)

print("Promedio:", promedio)
print("Cantidad de aprobados:", aprobados)
print("Cantidad de desaprobados:", desaprobados)