from PIL.ImageChops import offset

from db.config import Session
from db.models import *
from sqlalchemy import and_,desc



session = Session()


def menu ():
    while True:
        print("------------MENU-----------------------")
        print("1) para insertar un rol \n")
        print("2) listar todas las prioridades \n")
        print("3) prioridades filtrado por nombre \n")
        print("4) pruebas")

        print("5) PRUEBAS DE CONSULTAS EN CLASE")
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
        elif opc == 4:
            tareas = session.query(Tarea).filter(and_
                    (Tarea.sprint_id == 1, Tarea.estado_id == 1)).all()
            for tarea in tareas:
                print(tarea.titulo)
        elif opc == 5:
            '''tareas = session.query(Tarea).filter(Tarea.estimacion_horas > 2).limit(2).all()
            for tarea in tareas:
                print(f"{tarea.titulo}")

            while True:
                resp = input("¿Quieres otras dos?")

                if resp.lower() == "no":
                    print("adios")
                    break

                if resp.lower() == "si":
                    dosSiguientes = session.query(Tarea).filter(Tarea.estimacion_horas > 2).offset(2).limit(2).all()
                    for tarea in dosSiguientes:
                        print(f"{tarea.titulo}")
                else:
                    print("No has introducido la respuesta")
            #Preguntar si quiere otros dos y si la opcion es s que me de los dos siguientes

            
            print("------PROGRAMADOR----------")

            #BUSCAR PROGRAMADORES CUYO EMAIL ES "luis@empresa.com"
            programador = session.query(Programador).filter(Programador.email == "luis@empresa.com").first()
            print(programador)
            '''

        elif opc == 6:
            pass
            #ordenar las tareas la que tengan una mayor estimacion primero
            tareas = session.query(Tarea).all()
            for tarea in tareas:
                print(tarea.titulo + " "+tarea.prioridad.nombre)


        elif opc == 7:
            pass
            #Quiero devolver las tareas que son prioridad criticas
            tareas_criticas = session.query(
                Tarea.titulo, Prioridad.nombre,Tarea.sprint_id).join(Prioridad, Tarea.prioridad_id == Prioridad.id).filter(Prioridad.id == 3).all()
            for tareasC in tareas_criticas:
                print(tareasC)
        else:
            print("FIN SE ACABO")

if __name__ == '__main__':
    menu()