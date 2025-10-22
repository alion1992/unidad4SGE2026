from datetime import datetime
nombre = "Francisco"
fecha = datetime.now().strftime("%d%m%Y").lower()
nombre_fichero = f"log/{fecha}{nombre}_Persona.log"


print(fecha)

with open ("ejercicio/libro.txt", "r") as libro:
    while libro.readline():

        with open(nombre_fichero, "a") as f:
            pass

