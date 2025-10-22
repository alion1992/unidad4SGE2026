import matplotlib.pyplot as plt
alumnos = ["Francisco", "Jaime", "Alicia"]
edad = [33,53,51]
plt.bar(alumnos,edad)
plt.title("Edad de los alumnos")
plt.xlabel("Alumno")
plt.ylabel("Edad")
plt.show()