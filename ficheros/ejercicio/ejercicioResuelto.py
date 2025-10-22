
from datetime import datetime
from io import UnsupportedOperation
from opcode import opname

nombre = "Francisco"
fecha = datetime.now().strftime("%d%m%Y").lower()
nombre_fichero = f"log/{fecha}{nombre}_Persona.log"
print(nombre_fichero)

try:
    with open("libro.txt","r") as libro:
        try:
            with open(nombre_fichero,"a") as log:
                fila = libro.readline()


                while fila:
                    nuevo = fila.replace(" ",",")

                    log.write(f"\nInsert into Personas (id,Nombre, "
                              f"Apellidos, fecha_nacimiento,calle, "
                              f"codigo_postal, numero, movil, values "
                              f"(seq_personas.nextval(personas_seq, {nuevo})")
                    fila = libro.readline()
        except FileNotFoundError as error:
            print(f"El fichero LOG no se ha encontrado {error}")
        except UnsupportedOperation as error:
             print(f"No tienes permiso para realizar esa operacion {error}")
        except Exception as error:
             raise Exception
except FileNotFoundError as error:
    print(f"El fichero libro no se ha encontrado {error}")
except UnsupportedOperation as error:
    print(f"No tienes permiso para realizar esa operacion {error}")
except Exception as error:
    print(f"Se ha producido un error de aplicacion {error}")








