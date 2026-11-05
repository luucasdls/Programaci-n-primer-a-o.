class Figura:
    def area(self):
        pass


class Circulo(Figura):
    def __init__(self,radio):
        self.radio = radio
    def area(self):
        return 3.1416 * self.radio ** 2


class Cuadrado(Figura):
    def __init__(self,lado):
        self.lado = lado


    def area(self):
        return self.lado * self.lado


circulo1 = Circulo(3)
Cuadrado1 = Cuadrado(4)


print("Área del círculo:", circulo1.area())
print("Área del cuadrado:", Cuadrado1.area())
