class NegativeNumberError(Exception):
    pass
try:
    numero1 = int(input("Dame un número:"))

    if numero1 < 0:
        raise NegativeNumberError

    raiz_cuadrada = numero1 ** 0.5
    print("La raíz cuadrada de", numero1,"es:", raiz_cuadrada)
except NegativeNumberError:
    print("No se pueden calcular raíces cuadradas de números negativos.")