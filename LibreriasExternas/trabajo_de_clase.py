import random as rd
import numpy as np


'''
listaNp = np.array([1,2,3,4,5])
print(listaNp)
print(listaNp.mean())
listaBi = np.array([[1,2,3],[1,3,4]])
print(listaBi)

listaDeCeros = np.ones(3)
print(listaDeCeros)
'''
listaRandom = np.random.randint(5,20,(5,4))
'''5 filas y 4 columnas numeros aleatorios del 5 al 20'''
print(listaRandom)
print('--------------------------')
'''Mostrar la fila 3 completa'''
print(listaRandom[3,:-2])
'''Mostrar la columna 2 completa'''
print(listaRandom[:,2])





