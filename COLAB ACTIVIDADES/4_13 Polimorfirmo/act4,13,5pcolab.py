class Operacion:
    def resultado(self):
        pass


class Suma(Operacion):
    def __init__(self,a,b):
        self.a = a
        self.b = b


    def resultado(self):
        return self.a + self.b




class Multiplicacion(Operacion):
    def __init__(self,a,b):
        self.a = a
        self.b = b


    def resultado(self):
        return self.a * self.b
   


suma = Suma(2,2)
multiplicacion = Multiplicacion(2,2)


print(suma.resultado())
print(multiplicacion.resultado())
