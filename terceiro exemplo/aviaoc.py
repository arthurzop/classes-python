from aereo import aereo

class aviaoc(aereo):
    def __init__(self, carga, velocidade):
        super().__init__('aviao de carga', velocidade, 13000)
        self.__carga = carga

    def get_carga(self):
        return self.__carga
    
    def set_carga(self, carga):
        self.__carga = carga

    def carregar(self):
        print(f'Carregando o {self.get_nome()}')