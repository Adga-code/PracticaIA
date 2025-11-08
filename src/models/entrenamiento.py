import src.database.connect as connect
import src.modules.functions as f
from src.models.personaje import Pokemon
from src.services.interpreter import *
from time import sleep

while True:
    pokemon = Pokemon()
    acciones = []
    captura = False
    while True:
        
        print("POKEMON SALVAJE")
        hacer = accionar(acciones)
        print(f"---> {hacer}")
        sleep(2)
        print("---------------------------------------")
        match hacer:
            case "pokeball":
                captura = pokemon.pokeball()
                if captura:
                    print("POKEMON ATRAPADO")
                    acciones.append(hacer)
                    fin(acciones,"exito")
                    break
                else:
                    print("Fallo de captura")
                    acciones.append(hacer)
                    fin(acciones,"fracaso")
                    acciones = []
            case "roca":
                pokemon.roca()
                print("Posibilidad de captura aumentada")
                print("Posibilidad de huida aumentada")
                if "sebo" in acciones:
                    acciones = []
                else:
                    acciones.append(hacer)
            case "sebo":
                pokemon.sebo()
                print("Posibilidad de captura empeorada")
                print("Posibilidad de huida empeorada")
                if "roca" in acciones:
                    acciones = []
                else:
                    acciones.append(hacer)
        if pokemon.huir():
            print("El pokemon escapo")
            fin(acciones,"huida")
            break
    if captura:
        print("0 para salir")
        ado = input("---> ")
        f.s()
        if ado == "0":
            break
        
        
            
"""except:
            print("========================")
            print("Hubo un fallo")
            print("========================")
            continue

"""
