class Edificio:
    def __init__(self,numVentanas, numPuertas, pisos):
        self.numVentanas = numVentanas
        self.numPuertas = numPuertas
        self.pisos = pisos

    def caracteristicas(self):
        return f"Este edificio tiene {self.numVentanas} de ventanas {self.numPuertas} de puertas y {self.pisos} pisos"

class Instituto(Edificio):
    def __init__(self,numVentanas, numPuertas,
                 pisos,numAulas,numProfesores):
        super().__init__(numVentanas,numPuertas,pisos)
        self.numAulas = numAulas
        self.numProfesores = numProfesores

    def caracteristicas(self):
        return (f" {super().caracteristicas()} y {self.numAulas} "
                f"número de aulas y por último {self.numProfesores} de profesores")



virgenGracia = Instituto(30,40, 3, 20, 83)

print(virgenGracia.caracteristicas())


virgenGracia.numAulas = -1

print(virgenGracia.numAulas)

