class conta:

    def __init__(self, nome, senha, tipo, data, banco):
        self.nome = nome
        self.senha = senha
        self.tipo = tipo
        self.data = data
        self.banco = banco

    def sacar(self):
        print('ligando')

    def depositar(self):
        print('desligando')
    