from src.database import connect
from src.modules import functions
from src.models import *
from src.services import *



functions.s()
while True:
    while True:
        try:
            print("elige modo: 1 para entrenar, 2 para 'hablar', 0 para salir")
            opc = int(input("---> "))
            functions.s()
            if opc in [1,2, 0]:
                break
            else:
                functions.s()
                print("Ingresa una opcion valida.")
        except ValueError:
            functions.s()
            print("Ingresa un numero entero valido.")
    if opc == 1:
        import src.models.entrenamiento as entrenamiento
    elif opc == 2:
        import src.models.muestra as muestra
    else:
        break
    functions.s()