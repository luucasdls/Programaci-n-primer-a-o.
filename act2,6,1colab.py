aprobados = 0
desaprobados = 0

cantidad = int(input("¿Cuántos estudiantes hay? "))

for i in range(cantidad):
    nota = float(input("Ingrese la calificación: "))

    if nota >= 7:
        aprobados += 1
    else:
        desaprobados += 1

print("Cantidad de aprobados:", aprobados)
print("Cantidad de desaprobados:", desaprobados)