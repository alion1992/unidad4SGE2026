class Persona:
    def __init__(self,nombre,apellido,edad,correo):
        self.nombrePersona = nombre
        self.apellidoPersona = apellido
        self.edadPersona = edad
        self.__correo = correo

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        self.__correo = valor


    def __str__(self):
        return f" Soy {self.nombrePersona} {self.apellidoPersona} {self.edadPersona} {self.__correo}"

class Aula:
    def __init__(self):
        self.curso = "DAM2"
        self.numeroAlumnos = 14

persona = Persona("Francisco", "Alia", 33, "fran@gmail.com")
persona1 = Persona("Juan","Serna", 22, "dd@dd.es")
aula = Aula ()

persona.correo = "franActu"
print(persona.__dict__)

