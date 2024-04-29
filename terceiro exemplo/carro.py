from terrestre import terrestre

class carro(terrestre):
    def __init__(self, marca, velocidade):
        super().__init__('Carro', velocidade, 4)
        self.__marca = marca

    def get_marca(self):
        return self.__marca
    
    def set_marca(self, marca):
        self.__marca = marca

    def buzinar(self):
        print('Bii Biiii!')