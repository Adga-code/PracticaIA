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
        while True:
            try:
                print("Cuantos intentos? (-1 para infinitos)")
                intent = int(input("---> "))
                f.s()
                if intent < -1:
                    print("Ingrese un valor valido")
                    continue
                break
            except:
                f.s()
                print("Ingrese un valor valido")

        with open("src/services/historico.txt", "w") as f:
            f.write("==========================================\n")
        codigo("2025/11/08","practica",intent)
        f.s()