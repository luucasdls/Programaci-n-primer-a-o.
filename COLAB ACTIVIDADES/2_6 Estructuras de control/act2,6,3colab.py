import random
#Lista de corredores.
Pilotos = ["Leclerc", "Hamilton", "Verstappen", "Colapinto"]
#Distancias acumuladas por segundo.
Distancias = [0, 0, 0, 0]
#Duración de la carrera, las veces que se repetira el codigo.
for segundo in range(10):
    print("Segundo", segundo +1)
    #Recorriendo todos los pilotos y sus posiciones.
    for i in range(len(Pilotos)):
        #Genero una velocidad random por cada segundo que pase entre el numero 10 y 20.
        Velocidad = random.randint(10, 20)
        #Suma de la velocidad a la distancia final.
        Distancias[i] += Velocidad
        #Muestra que piloto es, a cuanto va y cuanto avanzo en ese segundo.
        print(Pilotos[i], "Va a la velocidad de", Velocidad, "Km/h" , "Va reccoriendo", Distancias[i] ,"en total")
        #Linea vacía en la cual separo segundos.
        print()
#Busco la mayor distancia recorrida por piloto.
maxima_distancia = max(Distancias)
print ("Carrera terminada")
print ("Distancia máxima:" , maxima_distancia)
#Lista donde guardo el ganador de la carrera.
Ganadores = []
#Reviso que pilotos tienen la mayor distancia para saber quien gano.
for i in range (len(Pilotos)):
    #Con este comando verifico si empatan en distancia los pilotos, se muestra un print con empate en la carrera.
    if Distancias[i] == maxima_distancia:
        Ganadores.append(Pilotos[i])
#Mostrar el resultado final de la carrera.
if len(Ganadores) == 1:
    print("El piloto ganador de la carrera es" , Ganadores [0])
else:
    print("Hay un empate entre los pilotos" , " , ".join(Ganadores))