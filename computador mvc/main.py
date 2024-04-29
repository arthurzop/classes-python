from computador import computador

pc1 = computador('Dell', 'Latitude 3420', 'Notebook', 4000, 'Intel', 'i5', 'Notebook', 'Fonte Externa', '14 in')


print(f'Marca:       {pc1.marca}')
print(f'Modelo:      {pc1.modelo}')
print(f'Tipo:        {pc1.tipo}')
print(f'Preço:       {pc1.preco}')
print(f'Processador: {pc1.processador}')
print(f'Gabinete:    {pc1.gabinete}')
print(f'Fonte:       {pc1.fonte}')
print(f'Monitor:     {pc1.monitor}')

pc1.ligar()
pc1.desligar()
pc1.jogar()
pc1.estudar()