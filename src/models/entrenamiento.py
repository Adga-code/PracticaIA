from src.models.personaje import Pokemon
from src.services.interpreter import *
from time import sleep


def codigo(fecha, tipo, intentos=-1):
    cond = False
    while True:
        if cond:
            break
        pokemon = Pokemon()
        acciones = []
        captura = False
        print("POKEMON SALVAJE")
        while True:
            if intentos!=-1:
                intentos-=1
                if intentos == 0:
                    cond = True
                    break
            hacer = accionar(acciones,tipo)
            print(f"---> {hacer}")
            sleep(1)
            print("---------------------------------------")
            match hacer:
                case "pokeball":
                    captura = pokemon.pokeball()
                    if captura:
                        print("POKEMON ATRAPADO")
                        acciones.append(hacer)
                        fin(acciones,"exito",fecha,tipo)
                        break
                    else:
                        print("Fallo de captura")
                        acciones.append(hacer)
                        fin(acciones,"fracaso",fecha,tipo)
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
                fin(acciones,"huida",fecha,tipo)
                break
            
        
        
            
"""except:
            print("========================")
            print("Hubo un fallo")
            print("========================")
            continue

"""
