f = open('ejemplo.txt', 'r')
print(f.readline())
f.close()


f = open('ejemplo.txt', 'w')
f.writelines('Estamos aqui')
f.close()

print('Empezamos con a')
f = open('ejemplo.txt', 'a')
f.writelines('\n hola')



print('Empezamos con a')
f = open('ejemplo.txt', 'r+')
while f.readline():
    print(f.readline())


