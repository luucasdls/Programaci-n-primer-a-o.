from datetime import datetime
#En estas dos variables, la fecha que escribamos solo es texto para python.
fecha1 = input("Ingrese la primer fecha, por ejemplo de la siguiente manera. (13/03/2020)")
fecha2 = input("Ingrese la segunda fecha, por ejemplo de la siguiente manera.(13/03/2021)")
#En estas dos variables con el comando "datetime.strptime" le indicamos al programa que valore al texto como fecha de calendario.
fecha1 = datetime.strptime(fecha1, "%d/%m/%Y")
fecha2 = datetime.strptime(fecha2, "%d/%m/%Y")
#Con la variable "diferencia" calculamos la diferencia entre fechas.
diferencia = fecha2 - fecha1
#Con el comando "diferencia.days" obtenemos la diferencia en días.
print("La diferencia es de: ", diferencia.days, "días.")