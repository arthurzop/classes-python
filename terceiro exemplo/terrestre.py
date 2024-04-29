from transporte import transporte

class terrestre(transporte):
    def __init__(self, nome, velocidade, rodas):
        super().__init__(nome, velocidade)
        self.__rodas = rodas

    def curva(self):
        print(f'{self.get_nome()} está fazendo curva a {self.get_velocidade()}km/h')