from src.database import connect
from random import choice, randint
import os

def fin(acciones, consecuencias, coleccion="entrenamiento"):
    #todo envia los datos del intento para futuras referencias
    data ={
        "acciones" : acciones,
        "consecuencias" : consecuencias,
        "estado" : "practica",
        "fecha" : "2025/11/08"
    }
    with open("src/services/historico.txt", "a") as f:
        f.write(f"{consecuencias}\n")
        f.write(f"2025/11/08\n")
        f.write("==========================================\n\n\n")
    connect.insert(connect.getCollection(coleccion), data)

def accionar(acciones, coleccion="entrenamiento"):
    #todo toma un decisión segun los datos pasados
    if randint(1,10) < 3:
        with open("src/services/historico.txt", "a") as f:
            random = choice(["pokeball","roca","sebo"])
            f.write("Uso al azar de 2 en 10\n")
            f.write(f"{random}\n")
            f.write("------------------------------\n")
        return random
    if acciones == []:
        datos = connect.getAll(connect.getCollection(coleccion)) #? da solo los datos que contengan las mismas acciones
    else:
        datos = connect.getSome(connect.getCollection(coleccion),{ "acciones": { "$all": acciones } }) #? da solo los datos que contengan las mismas acciones
    
    opciones = [] #? primera lista de opciones a tomar
    choices = []  #? version refinada de la lista anterior

    for x in datos:
        #? recorre la lista y limpea los datos que no empiecen con las mismas acciones
        if x["acciones"][0:len(acciones)] != acciones:
            continue #! Si no empieza igual a las acciones tomadas no lo considera

#! DE PRUEBAS
        cond = False
        for i in opciones:
            if x["acciones"] == i["acciones"]:
                if x["consecuencias"] == "exito":
                    i["exitos"] += 1
                i["cantidad"] += 1
                cond = True
                break
        if cond:
            continue

        if x["consecuencias"] == "exito":
            opciones.append({
                "acciones" : x["acciones"],
                "exitos" : 1,
                "cantidad" : 1})
        else:
            opciones.append({
                "acciones" : x["acciones"],
                "exitos" : 0,
                "cantidad" : 1})

    if opciones == []:
        with open("src/services/historico.txt", "a") as f:
            random = choice(["pokeball","roca","sebo"])
            f.write("Uso al azar por no tener historico\n")
            f.write(f"{random}\n")
            f.write("------------------------------\n")
        return random


    probabilidad = 0


    for x in opciones:
        calculo = (x["exitos"]*100) / x["cantidad"]
        if probabilidad < calculo:
            probabilidad = calculo
            choices=[x["acciones"][len(acciones)]]
        elif probabilidad == calculo and calculo > 0:
            choices.append(x["acciones"][len(acciones)])
    
    if choices == []:
        for i in opciones:
            if i["exitos"] != 0:
                choices.append(x["acciones"][len(acciones)])
        if choices == []:
            choices = ["pokeball","roca","sebo"]
        with open("src/services/historico.txt", "a") as f:
            random = choice(choices)
            f.write("Uso al azar por no tener historico\n")
            f.write(f"{random}\n")
            f.write("------------------------------\n")
        return random
#! DE PRUEBAS
    with open("src/services/historico.txt", "a") as f:
        f.write(f"{acciones}\n")
        elegido = choice(choices)
        f.write(f"Estos caminos tiene {elegido}\n")
        f.write("------------------------------\n")

    return elegido
        
