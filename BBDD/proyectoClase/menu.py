from db.config import Session
from db.models import Rol, Prioridad



session = Session()


def menu ():
    while True:
        print("1) para insertar un rol \n")
        print("2) listar todas las prioridades \n")
        print("3) prioridades filtrado por nombre \n")
        #OPCION 4 mapear la clase programadores y añadir que en la opcion 4 podais añadir un programador
        #con datos estaticos DEV de rol Consejo: programador.rol_id = 2
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

            for prioridad in prioridades:
                print(f"Nombre: {prioridad.nombre} ID: {prioridad.id}")
        elif opc == 3:
            prioridades = session.query(Prioridad).filter_by(nombre='LOW')
            for prioridad in prioridades:
                print(f"Nombre: {prioridad.nombre} ID: {prioridad.id}")
        else:
            break

    print("FIN SE ACABO")

if __name__ == '__main__':
    menu()