import src.database.connect as connect
from src.services.interpreter import respond_to_input
from random import randint

while True:
    while True:
        try:
            pre = int(input("---> "))
            if pre in [0,1,2,3,4,5]:
                break
            else:
                print("por favor ingresa un numero entre 0 y 5.")
        except ValueError:
            print("por favor ingresa un numero entero valido.")
            continue
    if pre == 0:
        break
    else:
        print(respond_to_input(pre))
