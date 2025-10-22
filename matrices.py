import uso_random as r

matriz = [1,2,3,4,5,6]
print(matriz)
print(type(matriz))
print(max(matriz))
print(len(matriz))

dimesion2 = [[1,2,3],[3,2,1],[2,3,0]]

for i in range (len(dimesion2)):
    for j in range (len(dimesion2[i])):
        print(f"Los elementos de la matriz son {dimesion2[i][j]}")

matriz.append(7)
print(matriz)
num = matriz.pop()
print(matriz)
#print(matriz.index(9))
print(matriz.count(2))
matriz.reverse()
print(matriz)