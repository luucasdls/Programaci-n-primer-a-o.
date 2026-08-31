#Desafío 7, convertidor de temperaturas de Celsius a Fahrenheit o Kelvin (Se considera grados celsius) 
try: #Se utilizan los comandos "try" y "except" para evitar errores del usuario al colocar letras o grafemas, guiandolo a usar numeros con el print ultimo.
    Celsius = float (input("Dame un numero cualquiera, yo te lo voy a convertir a Fahrenheit o Kelvin.")) #Se utiliza el comando float para permitir al usuario colocar numeros con decimales.
    #Calculo para transformar de Celsius a Fahrenheit.
    Fahrenheit = (Celsius * 9 / 5)+32
    #Calculo para transformar de Celsius a Kelvin.                                                         
    Kelvin = Celsius + 273.15
    print ("Temperatura convertida a Fahrenheit:", Fahrenheit)
    print ("Temperatura convertida a Kelvin:", Kelvin)
except:
        print ("Te pedi un numero, no una letra, intenta de nuevo porfavor.")