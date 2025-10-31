from src.models.personaje import Personaje

def combatir(pers1, pers2, msj, act): #todo msj=input que llega, act = respuesta de la IA
    accion1 = 0
    accion2 = 0

    match msj:
        case "atacar":
            accion1 = pers1.atacar()
        
        case "defender":
            accion1 = pers2.defender()
        
    match act:
        case "atacar":
            accion2 =pers2.atacar()
        case "defender":
            accion2 = pers2.defender()
    

    return [accion1,accion2]

