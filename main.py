import src.modules.functions as f
from src.models.entrenamiento import codigo

while True:
    try:
        print("(1) para practica")
        print("(2) para salir")
        opc = int(input("---> "))
        f.s()
        if opc in [1,2]:
            break
        else:
            print("ingrese valor valido")
    except:
        f.s()
        print("ingrese valor valido")
    
match opc:
    case 1:
        with open("src/services/historico.txt", "w") as f:
            f.write("==========================================\n")
        codigo()
        f.s()