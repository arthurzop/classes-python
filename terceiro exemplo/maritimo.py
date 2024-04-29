from transporte import transporte

class maritimo(transporte):
    def __init__(self, nome, velocidade, passageiros):
        super().__init__(nome, velocidade)
        self.__passageiros = passageiros

    def transportar(self):
        print(f'{self.get_nome()} transportando {self.__passageiros} passageiros.')