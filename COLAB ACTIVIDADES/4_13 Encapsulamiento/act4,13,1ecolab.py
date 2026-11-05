class Libro:
    def __init__(self,titulo,autor,ISBN):
        self._titulo = titulo
        self.autor = autor
        self.ISBN = ISBN

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self,nuevo_titulo):
        if self.titulo != nuevo_titulo:
            self._titulo = nuevo_titulo
        else:
            print("El titulo no puede ser igual al que ya existe.")

libro1 = Libro("Juanito", "Pedrito Picapiedras","5400")
print(libro1.titulo)

libro1.titulo = "Juanito"

