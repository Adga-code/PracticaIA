from random import randint

class Personaje:
    def __init__(self):
        self.vida = 10

    def atacar():
        posibilidad = randint(1, 10)
        if posibilidad in [1,2]:
            return 0  # Falló
        elif posibilidad in [3,4,5,6,7,8]:
            return 2  # Golpe débil
        elif posibilidad in [9,10]:
            return 3  # Golpe critico
    
    def defender():
        posibilidad = randint(1, 10)
        if posibilidad in [1,2]:
            return 0  # Recibe todo el daño
        elif posibilidad in [3,4,5,6,7,8]:
            return 1  # Bloqueo parcial
        elif posibilidad in [9,10]:
            return 2  # Bloqueo fuerte
    
    def recibir_danio(self, ataque):
        self.vida -= ataque
        return self.vida
    
    def huir():
        posibilidad = randint(1, 10)
        if posibilidad in [1,2]:
            return False  # Falló en huir
        elif posibilidad in [3,4,5,6,7,8,9,10]:
            return True  # Huyó con éxito
