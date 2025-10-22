'''
matriz = [1,2,3,4,5,6,7]
matrizDouble = [[1,2,3],[1,2,1],[7,9,8]]
print(matriz)

matriz.append(8)
print(matriz)
print("Antes del pop")
num = matriz.pop()
print("Despues del pop")
print(matriz)
print(f"este es el maximo {max(matriz)}")
print(f"este es el minimo {min(matriz)}")
print(f"esta es la longitud {len(matriz)}")
'''

matriz = [1,2,3,4,5,6,7]
matriz.reverse()
print(matriz)
#Numero de veces que aparece un numero
print(matriz.count(10))
print(matriz.index(11))
#imprimir cada uno de los valores de la matriz bidimensional
matrizDouble = [[1,2,3],[1,2,1],[7,9,8]]
