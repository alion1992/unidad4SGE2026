import random as r


def crear_Matriz():
    matriz = []
    for i in range(4):
        fila = []
        for j in range(4):
            fila.append(r.randint(1,10))
        matriz.append(fila)
    return matriz

def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j],end=" ")
        print()

matriz = crear_Matriz()
mostrar_matriz(matriz)