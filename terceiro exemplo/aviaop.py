from aereo import aereo

class aviaop(aereo):
    def __init__(self, capacidade, velocidade):
        super().__init__('aviao de passageiros', velocidade, 13000)
        self.__capacidade = capacidade

    def get_capacidade(self):
        return self.__capacidade
    
    def set_capacidade(self, capacidade):
        self.__capacidade = capacidade

    def decolar(self):
        print(f'{self.get_nome()} está decolando!')