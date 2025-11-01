from random import randint

class Pokemon:
    def __init__(self):
        self.captura = 100          #* 1-10 se captura a menor numero mas facil capturar
        self.huida = 100            #* 1-3 huye el poke a menor numero mas facil huir

    def pokeball(self):
        #todo intento de captura
        intento = randint(1, self.captura)
        if intento > 10:
            return False
        else:
            return True
        
    def roca(self):
        #todo lanzar roca, aumenta posibilidades de captura y posibilidades de huida
        if self.captura > 100:
            self.captura = 50
            self.huida = 50
        else:
            self.captura = round(self.captura/2)
            self.huida = round(self.huida/2)
    
    def sebo(self):
        #todo lanzar sebo, disminuye posibilidades de captura y posibilidades de huida
        if self.huida < 100:
            self.huida = 200
            self.captura = 200
        else:
            self.huida *= 2
            self.captura *= 2

    def huir(self):
        #todo intento de huir por parte del pokemon
        intento = randint(1,self.huida)
        if intento > 3:
            return True
        else:
            return False