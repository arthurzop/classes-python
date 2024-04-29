from pessoa import pessoa

class professor(pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def dar_aula(self):
        super().apresentar()
        print(f'Estou dando aula de {self.disciplina}')
