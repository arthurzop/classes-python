from maritimo import maritimo

class barco(maritimo):
    def __init__(self, capacidade, velocidade):
        super().__init__('Barco', velocidade, capacidade)
        self.__capacidade = capacidade

    def get_capacidade(self):
        return self.__capacidade
    
    def set_capacidade(self, capacidade):
        self.__capacidade = capacidade

    def embarcar(self):
        print(f'Embarcando {self.get_capacidade()} passageiros no {self.get_nome()}')
        