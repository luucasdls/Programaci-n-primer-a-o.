import string
import random

caracteres = string.ascii_letters + string.digits + string.punctuation
cadena = '' .join(random.choice(caracteres) for _ in range(8)) 
print("Cadena de 8 digitos randomizados.")
print(("-"),cadena)