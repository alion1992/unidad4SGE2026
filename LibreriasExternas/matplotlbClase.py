import matplotlib.pyplot as plt
profesores = ["Francisco", "Jaime", "Alicia"]
edad = [33,53,51]
plt.bar(profesores,edad)
plt.title("Edad de los profesores")
plt.xlabel("Nombre")
plt.ylabel("Edad")
plt.show()