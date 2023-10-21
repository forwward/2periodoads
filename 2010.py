class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco  # A associação acontece aqui


    def mostrar_informacoes(self):
        return f"(self.nome) mora em (self.endereco.mostrar_endereco())"

endereco_maria = endereco("Av. Principal", "São Paulo")
maria = Pessoa("Maria", endereco_maria)

print(maria.mostrar_informacoes)