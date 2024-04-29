class tv:

    def __init__(self, marca, modelo, preco, tela, cor, smart):
        self.marca = marca
        self.modelo = modelo
        self.preco = preco
        self.tela = tela
        self.cor = cor
        self.smart = smart

    def ligar(self):
        print('ligando')

    def desligar(self):
        print('desligando')
    
    def mudar(self):
        print('mudando de canal')