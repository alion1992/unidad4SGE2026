from db.config import Session
from db.models import Rol

session = Session()


def menu ():
    while True:
        print("1) para insertar un rol \n")
        print("2) salirme \n")

        opc = int(input("Dime que quieres hacer"))
        if opc == 1:
            nombreRol = input("Dame el nombre del rol")
            rol = Rol(nombre=nombreRol)
            session.add(rol)
            session.commit()
            print("Se ha guardado el rol correctamente\n")
        else:
            break

    print("FIN SE ACABO")

if __name__ == '__main__':
    menu()