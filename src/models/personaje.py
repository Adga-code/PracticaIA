from random import randint

class Pokemon:
    def __init__(self):
        self.ratioCaptura = 100          #* 1-10 se ratioCaptura a menor numero mas facil ratioCapturar
        self.ratioHuida = 100            #* 1-3 huye el poke a menor numero mas facil huir

    def pokeball(self):
        #todo intento de ratioCaptura
        intento = randint(1, self.ratioCaptura)
        if intento > 10:
            return False
        else:
            return True
        
    def roca(self):
        #todo lanzar roca, aumenta posibilidades de ratioCaptura y posibilidades de ratioHuida
        if self.ratioCaptura > 100:
            self.ratioCaptura = 50
            self.ratioHuida = 50
        else:
            self.ratioCaptura = round(self.ratioCaptura/2)
            self.ratioHuida = round(self.ratioHuida/2)
    
    def sebo(self):
        #todo lanzar sebo, disminuye posibilidades de ratioCaptura y posibilidades de ratioHuida
        if self.ratioHuida < 100:
            self.ratioHuida = 200
            self.ratioCaptura = 200
        else:
            self.ratioHuida *= 2
            self.ratioCaptura *= 2

    def huir(self):
        #todo intento de huir por parte del pokemon
        intento = randint(1,self.ratioHuida)
        print(self.ratioHuida)
        print(intento)
        if intento < 4:
            return True
        else:
            return False