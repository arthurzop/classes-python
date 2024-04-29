class celular:

    def __init__(self, marca, modelo, preco, so, tela):
        self.marca = marca
        self.modelo =  modelo
        self.preco = preco
        self.so = so
        self.tela = tela

    def ligar(self):
        print('ligando')
    
    def desligar(self):
        print('desligando')

    def telefonar(self):
        print('telefonando')

    def jogar(self):
        print('jogando')