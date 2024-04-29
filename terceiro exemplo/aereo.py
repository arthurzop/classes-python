from transporte import transporte

class aereo(transporte):
    def __init__(self, nome, velocidade, altitude):
        super().__init__(nome, velocidade)
        self.__altitude = altitude

    def altura(self):
        print(f'{self.get_nome()} está voando à {self.__altitude} pés.')