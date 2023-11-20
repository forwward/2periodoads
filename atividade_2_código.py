class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.cursos_lecionados = []

    def designar_curso(self, curso):
        self.cursos_lecionados.append(curso)
        curso.designar_professor(self)
        print(f'O professor {self.nome} foi designado para o curso {curso.nome}.')

    def listar_cursos_lecionados(self):
        print(f'Cursos lecionados por {self.nome}:')
        for curso in self.cursos_lecionados:
            print(f'- {curso.nome}')


class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.professor_designado = None

    def designar_professor(self, professor):
        self.professor_designado = professor

    def obter_professor(self):
        return self.professor_designado


professor1 = Professor("João")
professor2 = Professor("Maria")


curso1 = Curso("Matemática")
curso2 = Curso("História")
curso3 = Curso("Computação")


professor1.designar_curso(curso1)
professor2.designar_curso(curso2)
professor1.designar_curso(curso3)


professor1.listar_cursos_lecionados()
professor2.listar_cursos_lecionados()
