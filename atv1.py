class Caneta:
    def __init__(self, cor, dono):
        self.cor = cor
        self.dono = None

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.caneta = None
    
    def Pegar_caneta(self,caneta):
        self.caneta = caneta
        caneta.dono = self

pessoa1 = Pessoa("João")
caneta1 = Caneta("Azul")

pessoa1.Pegar_caneta(caneta1)
print(caneta1.dono)