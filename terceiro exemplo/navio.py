from maritimo import maritimo

class navio(maritimo):
    def __init__(self, carga, velocidade):
        super().__init__('navio', velocidade, 200)
        self.__carga = carga

    def get_carga(self):
        return self.__carga    
    
    def set_carga(self, carga):
        self.__carga = carga

    def carregar(self):
        print(f'{self.get_nome()} está carregando {self.__carga} toneladas.')