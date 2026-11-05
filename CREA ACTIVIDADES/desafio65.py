class Figura:
    def area(self):
        print("Las figuras tienen un área.")

class Circulo(Figura):
    def area(self):
        return ("El área del circulo es"), 3.14 * self.radio **2
    def __init__(self, radio):
        self.radio = radio


class Cuadrado(Figura):
    def area(self):
        return ("El área del cuadrado es:"), self.lado * self.lado
    def __init__(self,lado):
        self.lado = lado

circulo = Circulo(5)
cuadrado = Cuadrado(10)

figuras = [circulo,cuadrado]
#Podemos llamar a la misma característica area() sobre objetos distintos porque tanto "Circulo" como "Cuadrado" tienen esa característica,...
#pero cada clase lo implementa de una manera diferente. En "Circulo", area() utiliza PI o 3,14 * self.radio ** 2,...
#mientras que la clase "Cuadrado" utiliza self.lado * self.lado. Al recorrer la lista,...
#Python toma cada objeto y lo ejecuta automáticamente cada area dependiendo la versión de cada clase.
for figura in figuras:
    print(figura.area())
