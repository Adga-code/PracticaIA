from src.database import connect
from random import choice, randint  #! INVESTIGAR CHOICE

def fin(acciones, consecuencias, coleccion="entrenamiento"):
    #todo envia los datos del intento para futuras referencias
    data ={
        "acciones" : acciones,
        "consecuencias" : consecuencias
    }

    connect.insert(connect.getCollection(coleccion), data)

def accionar(acciones, coleccion):
    #todo toma un decisión segun los datos pasados


    datos = connect.getSome(connect.getCollection(coleccion),{ "acciones": { "$all": acciones } }) #? da solo los datos que contengan las mismas acciones
    
    opciones = [] #? primera lista de opciones a tomar
    choices = []  #? version refinada de la lista anterior

    for x in datos:
        #? recorre la lista y limpea los datos que no empiecen con las mismas acciones
        if x["acciones"][0:len(acciones)] != acciones:
            continue #! Si no empieza igual a las acciones tomadas no lo considera
        elif x["consecuencias"] == "fracaso":
            continue #! Si la lista lleva a fracaso no lo considera
        opciones.append({"paso" : x["acciones"][len(acciones)], "tiempo" : len(x["acciones"])})
    

    if opciones == []:
        #? si no hay rutas tomadas anteriormente similares a la actual, hace algo al azar
        return choice(["pokeball","roca","sebo"])
    

    temp = opciones[0]["tiempo"]
    for ddv in opciones:
        #? crea la segunda lista de opciones, las decisiones a tomar
        if ddv["tiempo"] > temp:
            continue #! Si toma mas pasos hacer las acciones que las decisiones actuales, no lo considera
        elif ddv["tiempo"] < temp:
            choices = [ddv["paso"]] #! Si toma menos tiempo que el resto, empieza de nuevo las opciones
        else:
            choices.append(ddv["paso"]) #! Si es de la misma calidad que el resto de las opciones anteriores la considera
    
    return choice(choices)
        
