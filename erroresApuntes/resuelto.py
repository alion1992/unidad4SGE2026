try:
    list = [1,2,3,4,5,6,5]

    opt = int(input("Dame el indice para ver que tiene la lista"))
    print(list[opt])
except ValueError as e:
    print(f"Se ha producido un error de valor {e}")
except IndexError as e:
    print(f"Se ha producido un error de tipo {e}")
except Exception:
    print("Error Exception")
finally:
    print("Se ha finalizado")
