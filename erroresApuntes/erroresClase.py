def controlarNumero(opcion):
    if opcion == "20":
        raise Exception("error de lo que quiero")

try:

    sumario = 20
    pedir = input("Dime un numero")
    controlarNumero(pedir)
    print("Se ha finalizado correctamente")
    #total = sumario + pedir

except ValueError as e:
    print(f"El numero introducido es incorrecto {e} ")
except TypeError as e:
    print(f"Se ha producido un error de tipo {e}")
except ZeroDivisionError as e:
    print(f'se ha producido un error {e}')
except Exception as e:
    print(f'se ha producido exception {e}')
finally:
    print("Se ha finalizado correctamente o no")
