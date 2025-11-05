from db.config import Session
from db.models import Rol, Prioridad



session = Session()


def menu ():
    while True:
        print("1) para insertar un rol \n")
        print("2) listar todas las prioridades \n")
        print("8) salirme \n")

        opc = int(input("Dime que quieres hacer"))
        if opc == 1:
            nombreRol = input("Dame el nombre del rol")
            rol = Rol(nombre=nombreRol)
            session.add(rol)
            session.commit()
            print("Se ha guardado el rol correctamente\n")
        elif opc == 2:
            prioridades = session.query(Prioridad).all()

            print("   ")
        else:
            break

    print("FIN SE ACABO")

if __name__ == '__main__':
    menu()