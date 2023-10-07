class livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
    def descricao(self):
        print(str(f"O livro '{self.titulo}' foi publicado em {self.ano_publicacao}, pelo autor '{self.autor}'.\n"))

livro1 = livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "1943")
livro1.descricao()

livro2 = livro("Divina Comédia", "Dante Alighieri", "1472")
livro2.descricao()
        