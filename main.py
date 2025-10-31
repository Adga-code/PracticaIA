from src.database import connect
from src.modules import functions
from src.models import *
from src.services import *



functions.s()
print("Welcome to the Application!")
while True:
    while True:
        try:
            print("Select mode: 1 for Training, 2 for Sample, 0 to Exit")
            opc = int(input("---> "))
            functions.s()
            if opc in [1,2, 0]:
                break
            else:
                functions.s()
                print("Please enter 1 or 2.")
        except ValueError:
            functions.s()
            print("Please enter a valid integer.")
    if opc == 1:
        import src.models.entrenamiento as entrenamiento
    elif opc == 2:
        import src.models.muestra as muestra
    else:
        break
    functions.s()