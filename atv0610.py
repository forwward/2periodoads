class Estudante:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def Apresentar(self):
        print(f"Meu nome é {self.nome} e minha idade é {self.idade}.")


aluno1 = Estudante("João", 18)
aluno1.Apresentar()



