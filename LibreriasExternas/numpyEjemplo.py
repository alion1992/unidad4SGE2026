import numpy as np


m1 = np.array([[1,2,3],[1,3,2]])
print(m1)

matrizCeros = np.zeros((3,3))
print(matrizCeros)
print(np.zeros(3))
m2 = np.arange(0,10,2)
print(m2)


m = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])

# elemento fila 0, col 1 → 20
print(m[0,1])
# toda la segunda columna → [20 50 80]
print(m[:,1])
# toda la segunda fila → [40 50 60]
print(m[1,:])
# submatriz [[20 30], [50 60]]
print(m[0:2, 1:3])

notas = np.array([5, 7, 8, 9, 6])
print("Media:", np.mean(notas))
print("Mediana:", np.median(notas))
print("Máximo:", np.max(notas))
print("Mínimo:", np.min(notas))
print("Desviación estándar:", np.std(notas))