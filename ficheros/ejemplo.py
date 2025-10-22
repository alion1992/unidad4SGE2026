#EJEMPLOS DE PERMISOS QUE CONOZCAMOS
#r, w, r+, a
'''
from io import UnsupportedOperation

try:
    file = open("fichero_de_prueba.txt", "r")
    linea = file.readline()
    while linea:
        print(linea)
        linea = file.readline()
    file.write("Adios")
    file.close()
except FileNotFoundError as e:
    print("No encuentro el fichero")
except UnsupportedOperation as e:
    print(f"No tengo permiso para esa operacion {e}")
finally:
    pass

'''

file = open("fichero_de_prueba.txt", "a")
file.write("Me lo voy a cargar\n")
file.close()


with open("fichero_de_prueba.txt", "a") as file:
    file.write("Me lo voy a cargar\n")

