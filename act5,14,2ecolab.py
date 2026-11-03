import math

class NegativeNumberError(Exception):
    pass

class LargeNumberError(Exception):
    pass

try:
    numero = int(input("Ingresa un número: "))

    if numero < 0:
        raise NegativeNumberError

    if numero > 30:
        raise LargeNumberError

    factorizacion = math.factorial(numero)

    print("El factorial de", numero, "es:", factorizacion)

except NegativeNumberError:
    print("Error: No se permiten números negativos.")

except LargeNumberError:
    print("Error: No se permiten números mayores a 30.")

except ValueError:
    print("Error: Solo puedes ingresar números enteros.")