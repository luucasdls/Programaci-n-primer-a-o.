# Desafío 4 de la ficha 1.
entrada = input ("Ingresa números separados por comas porfavor: ")
numeros = list (map(int, entrada.split(",")))
contador = 0
for numero in numeros:
    if numero % 2 == 0:
        contador = contador + 1
print ("Los números pares que me diste son:", contador)