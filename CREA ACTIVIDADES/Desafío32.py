#Función para verificar si un número es primo.
def es_primo(numero):
    if numero <= 1:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True
#Función para añadir cuantos números primos tenemos en total.
def contar_primos(n):
    contador = 0

    for numero in range(2, n + 1):
        if es_primo(numero):
            contador += 1

    return contador
#Función para mostrar en terminal que numeros del 1 al n son los primos.
def mostrar_primos(n):
    for numero in range(2, n +1):
        if es_primo(numero):
            print(numero)
#Función main que nos sirve para ordenar los códigos.
def main():
    n = int(input("Ingrese un número: "))

    cantidad = contar_primos(n)

    print(f"Entre 1 y {n} hay {cantidad} números primos.")

    print("Y los números primos son:")
    mostrar_primos(n)



main()