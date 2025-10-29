class Persona:
    def __init__(self, nombre,apellidos,calle):
        self.nombre = nombre
        self.apellidos = apellidos
        self.__calle = calle

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

    def saludo(self):
        print(f"Hola soy {self.nombre}")
    '''
    @property
    def calle(self):
        return self.__calle

    @calle.setter
    def calle(self, valor):
        self.__calle = valor'''





class Alumno(Persona):

    def __init__(self,nombre,apellidos,calle,curso):
        super().__init__(nombre,apellidos,calle)
        self.curso = curso
    '''def saludo(self):
        return f"Hola soy {self.nombre} del curso {self.curso}"'''


persona = Persona("Fran", "Alia",'ww')

print(persona.nombre)

persona.edad = 33
persona.calle =22
print(persona.edad)
print(persona.calle)
print(persona.__str__())
print(persona.__dict__)

alumno = Alumno("Fran", "Alia", "cc", "DAW2")

print(alumno.saludo())