from src.database import connect
from random import choice, randint  #! INVESTIGAR CHOICE

def pruebaError(accion, reaccion, efecto, colleccion = "entrenamiento"):
    #todo accion = que hizo el rival, reaccion = como responde la IA
    #todo efecto = consecuencias numericas [vida perdida, daño hecho]
    data = {"accionUs" : accion, "reaccion" : reaccion, 
            efecto : {"vida" : efecto["vida"], "daño" : efecto["daño"]} }
    connect.insert(connect.getCollection(colleccion), data)

def accionar(accion, colleccion = "entrenamiento"):
    
    data = connect.getSome(connect.getCollection(colleccion), {"accionUS" : accion})
    prop = -100
    reaccion = []
    for x in data:
        temp = (x["efecto"]["vida"]+1) / (x["efectp"]["daño"]+1)
        if temp > prop:
            reaccion = [x["reaccion"]]
            prop = temp
        elif temp == prop:
            reaccion.append(x["reaccion"])
    print(reaccion)
    return choice(reaccion)