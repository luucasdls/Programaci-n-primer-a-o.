import numpy as np 
import random
#En la variante tablero, genero la tabla de 5 filas por 5 columnas(5x5), 0 = No hay barco en la casilla, 1 = Si hay barco en la casilla.
tablero = np.zeros((5,5), dtype=int)
for i in range(3):
    fila = random.randint(0, 4)   
    columna = random.randint(0, 4)
    #Con la función "while" evaluo si ya hay un barco en la casilla del nuevo spawn, si hay, se sigue generando en otra casilla los barcos restantes.
    while tablero[fila][columna] == 1:
        fila = random.randint(0, 4)
        columna = random.randint(0, 4)
    tablero[fila][columna] = 1
print("Tablero inicial:")
print(tablero)
def disparar(x,y):
    if tablero[x][y] == 1:
        tablero[x][y] = 0
        print("BOOOOOM, barco neutralizado general.")
        return True
        print("Barcos restantes:", barcos_restantes)
    else:
        print("Hemos errado el tiro, probemos de nuevo.")
        return False
        print("Barcos restantes:", barcos_restantes)
#Variable para tener en cuenta los barcos restantes.
barcos_restantes = 3
#Bucle para que el programa se acabe cuando no hayan más barcos.
while barcos_restantes >0:
    fila_disparo = int(input("Ingrese una fila (0,4):"))
    columna_disparo = int(input("Ingrese una columna (0,4):"))
    if disparar(fila_disparo, columna_disparo):
        barcos_restantes -= 1
        print("Barcos restantes:", barcos_restantes)
print("Victoria, hemos destruido todos los barcos enemigos.")