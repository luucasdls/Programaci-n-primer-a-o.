numeros = []
for i in range(3):
    respuesta = int(input("Dame un número"))
    numeros.append(respuesta)

numeros.sort(reverse=True)

if numeros[0] == numeros[1] == numeros[2]:
    print("Los tres números son iguales:", numeros[0])
else:
    print("El mayor número de la lista es:", numeros[0])