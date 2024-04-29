from pessoa import pessoa

class estudante(pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def apresentar(self):
        super().apresentar()
        print(f'Estou estudando {self.curso}.')


