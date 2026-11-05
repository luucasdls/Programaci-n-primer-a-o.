class Usuario:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
class Bibliotecario(Usuario):
    def __init__(self, nombre, edad,seccion,años_experiencia):
        super().__init__(nombre, edad)
        self.seccion = seccion
        self.años_experiencia = años_experiencia
    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Sección:", self.seccion)
        print("Años de experiencia:", self.años_experiencia)

usuario = Bibliotecario("Juan","23","Filosofía","2 años de experiencia.")
usuario.mostrar_datos()