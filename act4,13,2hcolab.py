class Escritor:
    def __init__(self, nombre, genero, **kwargs):
        super().__init__(**kwargs)
        self.nombre = nombre
        self.genero = genero




class Academico:
    def __init__(self, area_investigacion, institucion, **kwargs):
        super().__init__(**kwargs)
        self.area_investigacion = area_investigacion
        self.institucion = institucion




class EscritorAcademico(Escritor, Academico):
    def __init__(self, nombre, genero, area_investigacion, institucion):
        super().__init__(
            nombre=nombre,
            genero=genero,
            area_investigacion=area_investigacion,
            institucion=institucion
        )


    def publicar_articulo(self, titulo):
        print(f"{self.nombre} publicó el artículo: {titulo}")




persona = EscritorAcademico(
    "Lucas",
    "Ciencia ficción",
    "Informática",
    "Universidad"
)


persona.publicar_articulo("Introducción a la programación.")


print(persona.nombre)
print(persona.genero)
print(persona.area_investigacion)
print(persona.institucion)
