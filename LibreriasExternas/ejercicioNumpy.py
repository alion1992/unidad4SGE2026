import numpy as np

notas = np.random.uniform(0, 10, (5, 4))
print(notas)
medias_alumnos = np.mean(notas, axis=1)
print(medias_alumnos)
medias_asignaturas = np.mean(notas, axis=0)
aprobados = np.sum(notas >= 5)
print(aprobados)