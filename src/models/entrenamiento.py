import src.database.connect as connect
from src.services.interpreter import train_model
from random import randint
from time import sleep

automatico = False

while True:
    while True:
        try:
            pre = randint(1,5)
            print(pre)
            if automatico:
                res = 6 - pre
                print(f"---> {res}")
                sleep(2)
            else:
                res = int(input("---> "))
            if res == 15:
                print("MODO AUTOMATICO ACTIVADO")
                sleep(2)
                automatico = True
                continue
            
            if res in [0,1,2,3,4,5]:
                break
            else:
                print("Please enter a number between 0 and 5.")
        except ValueError:
            print("Please enter a valid integer.")
            continue
    if res == 0:
        break
    else:
        train_model(pre, res)
