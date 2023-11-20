class Cabeça:
    def __init__(self, cor_olhos, expressao):
        self.cor_olhos = cor_olhos
        self.expressao = expressao

    def exibir_informacoes(self):
        print(f'Cabeça: Olhos {self.cor_olhos}, Expressão: {self.expressao}')


class Boneco:
    def __init__(self, cor_corpo, material):
        self.cor_corpo = cor_corpo
        self.material = material
        self.cabeca = Cabeça(cor_olhos='azuis', expressao='neutra')  

    def destruir_boneco(self):
        print('O boneco foi destruído.')
        del self.cabeca  

    def exibir_informacoes(self):
        print(f'Boneco: Corpo {self.cor_corpo}, Material: {self.material}')
        self.cabeca.exibir_informacoes()


boneco1 = Boneco(cor_corpo='vermelho', material='plástico')

boneco1.exibir_informacoes()

boneco1.destruir_boneco()
