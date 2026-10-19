class Libro:
    def __init__(self,titulo, autor):
        self.titulo = titulo
        self.autor = autor


class LibroEspecializado(Libro):
    def __init__(self, titulo, autor, campo_estudio, nivel_especializacion):
        super().__init__(titulo, autor)
        self.campo_estudio = campo_estudio
        self.nivel_especializacion = nivel_especializacion


Libro1 = LibroEspecializado(
    "Py desde cero",
    "Lucas de los Santos",
    "Informática",
    "Básico"
    )


print(Libro1.titulo)
print(Libro1.autor)
print(Libro1.campo_estudio)
print(Libro1.nivel_especializacion)
