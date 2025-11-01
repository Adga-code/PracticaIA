import src.database.connect as connect
import src.modules.functions as f
from src.models.personaje import Pokemon
from src.services.interpreter import *
from random import randint

while True:
    print("0 para salir")
    ado = input("---> ")
    f.s()
    if ado == "0":
        break
    pokemon = Pokemon()
    while True:
        try:
            print("POKEMON SALVAJE")

        except:
            break


